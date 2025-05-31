import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import os
import csv
import json

CONFIG_PATH = "tools/network_scanner/config.json"

def load_config():
    try:
        with open(CONFIG_PATH) as f:
            return json.load(f)
    except Exception:
        return {}

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

CONFIG = load_config()
SCAN_DIR = CONFIG.get("output_path", "/home/pi/network_scans")

def run_scan():
    subprocess.run(["python3", "tools/network_scanner/scanner.py"])
    messagebox.showinfo("Scan Complete", "Network scan finished and saved.")

def view_logs():
    try:
        files = [f for f in os.listdir(SCAN_DIR) if f.endswith(".csv")]
        latest_file = sorted(files)[-1]
    except (IndexError, FileNotFoundError):
        messagebox.showinfo("No Logs", "No scan files found.")
        return

    filepath = os.path.join(SCAN_DIR, latest_file)
    log_window = tk.Toplevel()
    log_window.title(f"Log: {latest_file}")
    log_window.geometry("320x240")
    text = tk.Text(log_window, wrap="none", font=("Courier", 10))
    text.pack(expand=True, fill="both")

    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            text.insert(tk.END, "\t".join(row) + "\n")

def set_scan_range():
    current_range = CONFIG.get("scan_range", "10.46.12.0/24")
    new_range = simpledialog.askstring("Set Scan Range", "Enter CIDR (e.g. 192.168.1.0/24):", initialvalue=current_range)
    if new_range:
        CONFIG["scan_range"] = new_range
        save_config(CONFIG)
        messagebox.showinfo("Scan Range Updated", f"Scan range set to: {new_range}")

def close_gui():
    root.destroy()

root = tk.Tk()
root.title("Network Scanner")
root.geometry("320x240")
root.configure(bg="black")

label = tk.Label(root, text="Network Scanner", font=("Helvetica", 16), fg="white", bg="black")
label.pack(pady=10)

scan_btn = tk.Button(root, text="Start Scan", font=("Helvetica", 14), width=20, height=2, command=run_scan)
scan_btn.pack(pady=5)

range_btn = tk.Button(root, text="Set Scan Range", font=("Helvetica", 12), width=20, height=2, command=set_scan_range)
range_btn.pack(pady=5)

log_btn = tk.Button(root, text="View Logs", font=("Helvetica", 12), width=20, height=2, command=view_logs)
log_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Back to Menu", font=("Helvetica", 12), width=20, height=2, command=close_gui)
exit_btn.pack(pady=15)

root.mainloop()