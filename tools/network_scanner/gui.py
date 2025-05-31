import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import csv

SCAN_DIR = os.path.expanduser("~/Documents/network_scans")  # Temp path for macOS dev

def run_scan():
    subprocess.run(["python3", "tools/network_scanner/scanner.py"])
    messagebox.showinfo("Scan Complete", "Network scan finished and saved.")

def view_logs():
    try:
        latest_file = sorted([
            f for f in os.listdir(SCAN_DIR) if f.endswith(".csv")
        ])[-1]
    except IndexError:
        messagebox.showinfo("No Logs", "No scan files found.")
        return

    filepath = os.path.join(SCAN_DIR, latest_file)

    # Create new window
    log_window = tk.Toplevel()
    log_window.title(f"Log: {latest_file}")
    log_window.geometry("320x240")
    text = tk.Text(log_window, wrap="none", font=("Courier", 10))
    text.pack(expand=True, fill="both")

    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            text.insert(tk.END, "\t".join(row) + "\n")

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

log_btn = tk.Button(root, text="View Logs", font=("Helvetica", 12), width=20, height=2, command=view_logs)
log_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Back to Menu", font=("Helvetica", 12), width=20, height=2, command=close_gui)
exit_btn.pack(pady=15)

root.mainloop()