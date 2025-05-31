import subprocess
import os
import csv
import json
from datetime import datetime

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
    except subprocess.CalledProcessError as e:
        return ""

def parse_arp_output(output):
    results = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) == 3 and parts[0].count('.') == 3:
            ip, mac, vendor = parts
            results.append((ip, mac))
    return results

def save_results(results, output_path):
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_path, f"scan_{timestamp}.csv")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "IP Address", "MAC Address"])
        for ip, mac in results:
            writer.writerow([timestamp, ip, mac])

def main():
    config = load_config()
    scan_range = config.get("scan_range", "10.46.12.0/24")
    output_path = config.get("output_path", "/home/pi/network_scans")
    print(f"Scanning network range: {scan_range}")
    output = run_arp_scan(scan_range)
    results = parse_arp_output(output)
    save_results(results, output_path)
    print(f"Scan complete. {len(results)} device(s) found.")

if __name__ == "__main__":
    main()
