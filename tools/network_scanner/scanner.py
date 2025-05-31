import subprocess
import os
import csv
import json
import socket
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

CONFIG_FILE = "tools/network_scanner/config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def run_arp_scan(scan_range):
    try:
        output = subprocess.check_output(
            ["sudo", "arp-scan", "--interface=eth0", scan_range],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return output
    except subprocess.CalledProcessError:
        return ""

def parse_arp_output(output):
    results = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) == 3 and parts[0].count('.') == 3:
            ip, mac, _ = parts
            results.append((ip, mac))
    return results

def probe_ports(ip, timeout=0.5):
    protocols = []
    ports = {
        "Modbus": 502,
        "BACnet": 47808
    }
    for name, port in ports.items():
        try:
            with socket.create_connection((ip, port), timeout=timeout):
                protocols.append(name)
        except Exception:
            continue
    return ", ".join(protocols) if protocols else "Unknown"

def save_results(results, output_path):
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_path, f"scan_{timestamp}.csv")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "IP Address", "MAC Address", "Protocol"])
        for ip, mac, proto in results:
            writer.writerow([timestamp, ip, mac, proto])
    return len(results)

def main():
    config = load_config()
    scan_range = config.get("scan_range", "10.46.12.0/24")
    output_path = config.get("output_path", "/home/pi/network_scans")
    output = run_arp_scan(scan_range)
    raw_results = parse_arp_output(output)
    enriched_results = []
    for ip, mac in raw_results:
        proto = probe_ports(ip)
        enriched_results.append((ip, mac, proto))
    count = save_results(enriched_results, output_path)

    # Show popup summary
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Scan Complete", f"Scan complete. {count} device(s) found.")

if __name__ == "__main__":
    main()
