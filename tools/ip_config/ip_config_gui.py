
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import re

def get_current_eth0_settings():
    try:
        output = subprocess.check_output("ip -4 addr show eth0", shell=True).decode()
        ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/(\d+)', output)
        if not ip_match:
            return [10, 46, 12, 2], 24
        ip_str, cidr = ip_match.groups()
        ip_parts = list(map(int, ip_str.split('.')))
        return ip_parts, int(cidr)
    except Exception:
        return [10, 46, 12, 2], 24

def get_default_gateway():
    try:
        output = subprocess.check_output("ip route | grep default", shell=True).decode()
        gw_match = re.search(r'default via (\d+\.\d+\.\d+\.\d+)', output)
        if gw_match:
            return list(map(int, gw_match.group(1).split('.')))
        return [10, 46, 12, 1]
    except Exception:
        return [10, 46, 12, 1]

class IPConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Static IP Config")
        self.root.geometry("320x240")
        self.root.configure(bg="black")

        self.ip, self.subnet = get_current_eth0_settings()
        self.gateway = get_default_gateway()

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="Set Static IP (eth0)", font=("Helvetica", 14), bg="black", fg="white")
        title.pack(pady=5)

        self.ip_labels = []
        ip_frame = tk.Frame(self.root, bg="black")
        ip_frame.pack(pady=2)
        for i in range(4):
            col = tk.Frame(ip_frame, bg="black")
            col.pack(side="left", padx=2)
            tk.Button(col, text="▲", command=lambda i=i: self.change_octet(self.ip, i, 1)).pack()
            lbl = tk.Label(col, text=str(self.ip[i]), font=("Helvetica", 10), width=3, bg="white")
            lbl.pack()
            self.ip_labels.append(lbl)
            tk.Button(col, text="▼", command=lambda i=i: self.change_octet(self.ip, i, -1)).pack()

        subnet_frame = tk.Frame(self.root, bg="black")
        subnet_frame.pack(pady=3)
        tk.Label(subnet_frame, text="Subnet /", font=("Helvetica", 11), bg="black", fg="white").pack(side="left")
        self.subnet_lbl = tk.Label(subnet_frame, text=str(self.subnet), font=("Helvetica", 11), width=2, bg="white")
        self.subnet_lbl.pack(side="left", padx=4)
        tk.Button(subnet_frame, text="▲", command=lambda: self.change_subnet(1)).pack(side="left")
        tk.Button(subnet_frame, text="▼", command=lambda: self.change_subnet(-1)).pack(side="left")

        self.gw_labels = []
        gw_frame = tk.Frame(self.root, bg="black")
        gw_frame.pack(pady=3)
        for i in range(4):
            col = tk.Frame(gw_frame, bg="black")
            col.pack(side="left", padx=2)
            tk.Button(col, text="▲", command=lambda i=i: self.change_octet(self.gateway, i, 1)).pack()
            lbl = tk.Label(col, text=str(self.gateway[i]), font=("Helvetica", 10), width=3, bg="white")
            lbl.pack()
            self.gw_labels.append(lbl)
            tk.Button(col, text="▼", command=lambda i=i: self.change_octet(self.gateway, i, -1)).pack()

        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Apply & Reboot", font=("Helvetica", 10), command=self.apply_and_reboot).pack(pady=2)
        tk.Button(btn_frame, text="Apply w/o Reboot", font=("Helvetica", 10), command=self.apply_and_restart).pack(pady=2)
        tk.Button(btn_frame, text="Back to Menu", font=("Helvetica", 10), command=self.root.destroy).pack(pady=5)

    def change_octet(self, target, index, delta):
        target[index] = (target[index] + delta) % 256
        if target is self.ip:
            self.ip_labels[index].config(text=str(target[index]))
        else:
            self.gw_labels[index].config(text=str(target[index]))

    def change_subnet(self, delta):
        self.subnet = min(30, max(1, self.subnet + delta))
        self.subnet_lbl.config(text=str(self.subnet))

    def write_config(self):
        ip_str = ".".join(map(str, self.ip)) + f"/{self.subnet}"
        gateway_str = ".".join(map(str, self.gateway))
        conf_block = (
            f"\ninterface eth0\n"
            f"static ip_address={ip_str}\n"
            f"static routers={gateway_str}\n"
            f"static domain_name_servers=8.8.8.8\n"
        )
        try:
            with open("/etc/dhcpcd.conf", "r") as f:
                lines = f.readlines()

            with open("/etc/dhcpcd.conf", "w") as f:
                skip = False
                for line in lines:
                    if line.startswith("interface eth0"):
                        skip = True
                    elif skip and line.startswith("interface"):
                        skip = False
                        f.write(line)
                    elif not skip:
                        f.write(line)
                f.write(conf_block)
            return ip_str
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write config:\n{e}")
            return None

    def apply_and_reboot(self):
        ip_str = self.write_config()
        if ip_str:
            reboot = messagebox.askyesno("Reboot?", f"IP set to {ip_str}\nReboot now?")
            if reboot:
                os.system("sudo reboot")

    def apply_and_restart(self):
        ip_str = self.write_config()
        if ip_str:
            subprocess.run(["sudo", "systemctl", "restart", "dhcpcd"])
            messagebox.showinfo("Success", f"IP set to {ip_str}\nNetworking restarted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IPConfigurator(root)
    root.mainloop()
