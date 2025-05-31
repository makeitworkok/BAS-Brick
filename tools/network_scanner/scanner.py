from datetime import datetime
import csv
import os
import json

def load_config():
    try:
        with open("tools/network_scanner/config.json") as f:
            return json.load(f)
    except Exception:
        return {}

def dummy_scan():
    config = load_config()
    output_dir = config.get("output_path", "/home/pi/network_scans")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(output_dir, f"scan_{timestamp}.csv")

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp", "ip", "mac"])
        writer.writerow([timestamp, "192.168.1.10", "AA:BB:CC:DD:EE:FF"])
        writer.writerow([timestamp, "192.168.1.20", "11:22:33:44:55:66"])

if __name__ == "__main__":
    dummy_scan()