import tkinter as tk
import subprocess
import os

class BASBrickLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BAS-Brick Launcher")
        self.geometry("320x240")
        self.build_gui()

    def build_gui(self):
        tk.Label(self, text="BAS-Brick Tools", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Set Static IP (eth0)", width=25, command=self.launch_ip_config).pack(pady=5)
        tk.Button(self, text="Set Scan Range", width=25, command=self.launch_scan_range).pack(pady=5)
        tk.Button(self, text="Run Network Scan", width=25, command=self.run_network_scan).pack(pady=5)

    def launch_ip_config(self):
        subprocess.Popen(["python3", "tools/network_scanner/ip_config_gui.py"])

    def launch_scan_range(self):
        subprocess.Popen(["python3", "tools/network_scanner/scan_range_gui.py"])

    def run_network_scan(self):
        subprocess.Popen(["sudo", "python3", "tools/network_scanner/scanner.py"])

if __name__ == "__main__":
    app = BASBrickLauncher()
    app.mainloop()
