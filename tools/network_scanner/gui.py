import tkinter as tk
from tkinter import messagebox
import subprocess

def start_scan():
    subprocess.run(["sudo", "python3", "tools/network_scanner/scanner.py"])
    messagebox.showinfo("Scan Complete", "Network scan finished.\nResults saved.")

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Network Scanner")
root.geometry("320x240")
root.configure(bg="black")

label = tk.Label(root, text="Network Scanner", font=("Helvetica", 16), fg="white", bg="black")
label.pack(pady=20)

scan_btn = tk.Button(root, text="Start Scan", font=("Helvetica", 14), width=20, height=2, command=start_scan)
scan_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Back to Menu", font=("Helvetica", 12), width=20, height=2, command=close_window)
exit_btn.pack(pady=20)

root.mainloop()