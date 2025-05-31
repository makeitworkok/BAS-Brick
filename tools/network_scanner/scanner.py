from datetime import datetime
import csv
import os

def dummy_scan():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = "/home/pi/network_scans"
    os.makedirs(output_dir, exist_ok=True)
    filepath = f"{output_dir}/scan_{timestamp}.csv"

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp", "ip", "mac"])
        writer.writerow([timestamp, "192.168.1.10", "AA:BB:CC:DD:EE:FF"])
        writer.writerow([timestamp, "192.168.1.20", "11:22:33:44:55:66"])

if __name__ == "__main__":
    dummy_scan()