# BAS-Brick

**BAS-Brick** is a portable, touchscreen-based field diagnostic tool for Building Automation Systems. It is designed to run on a Raspberry Pi 5 with a 3.5" touchscreen display. The first tool in the suite is a network scanner that detects BACnet/IP and Modbus TCP devices over a wired LAN using ARP scanning.

---

## 🚀 Features

### ✅ Core Functionality
- Real-time ARP-based device discovery on Ethernet (`eth0`)
- Automatically logs:
  - IP Address
  - MAC Address
  - Detected Protocol (BACnet, Modbus, or Unknown)
  - Timestamp
- Logs saved as CSV files under `/home/pi/network_scans/`

### 🛠 Touchscreen-Friendly GUI Tools
- **Launcher Menu**: Simple touchscreen interface with buttons
- **Set Static IP (eth0)**: Stylus-optimized per-octet control with press-and-hold acceleration
- **Set Scan Range**: Same input method as IP config
- **Run Network Scan**: Triggers ARP scan and probes discovered devices for BACnet/Modbus ports

---

## 🖥 Project Structure

```
BAS-Brick/
├── bas_brick_launcher.py             # Main menu GUI
└── tools/
    └── network_scanner/
        ├── scanner.py               # ARP + BACnet/Modbus scan tool
        ├── scan_range_gui.py       # GUI to set scan range
        ├── ip_config_gui.py        # GUI to set static IP for eth0
        ├── config.json             # Stores scan range and optional settings
```

---

## 📸 Example Output (CSV)

```
Timestamp,IP Address,MAC Address,Protocol
2025-05-31_14-32-11,10.46.12.101,B8:27:EB:12:34:56,BACnet
2025-05-31_14-32-11,10.46.12.102,B8:27:EB:65:43:21,Modbus
```

---

## ⚙️ Default Configuration

- Static IP: `10.46.12.2/24` on `eth0`
- Gateway: `.1` of the selected subnet (e.g., `10.46.12.1`)
- Wi-Fi (`wlan0`) remains DHCP
- Scan range: `/24` subnet (e.g., `10.46.12.0/24`)

---

## 🧪 Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/makeitworkok/BAS-Brick.git
cd BAS-Brick
```

### 2. Run the Launcher
```bash
python3 bas_brick_launcher.py
```

### 3. Buttons Available
- `Set Static IP (eth0)`
- `Set Scan Range`
- `Run Network Scan`

All tools are designed for 3.5" touchscreen operation with a stylus or finger.

---

## 🔒 Notes
- Designed for offline use (no Internet required)
- Ideal for field deployment on construction sites or industrial LANs
- Port probing is minimal and non-intrusive

---

## 🛣 Roadmap
- Log viewer (deferred)
- Service tagging and asset labeling
- Wireless discovery mode
- Additional field tools

---

## 📜 License
TBD — Will add when finalized.

---

## 🤝 Contributing
This project is tailored to Trane field needs, but general feedback and PRs are welcome.

Chris Favre
christopher.a.favre@gmail.com

