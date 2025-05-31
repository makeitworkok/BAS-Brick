# BAS-Brick

**BAS-Brick** is a modular, field-ready toolkit designed to run on a Raspberry Pi 5 with a touchscreen interface. It is intended for Building Automation System (BAS) professionals who need portable, easy-to-use tools for diagnostics, discovery, and troubleshooting in the field.

This project is designed with non-technical users in mind: large buttons, simple navigation, and automated functions — all accessible via a 3.5" touchscreen display (or HDMI monitor during development).

---

## 🔧 Current Toolset

### 🛠️ Tool 1: Network Scanner
- Scans a known subnet (e.g., `10.46.12.0/24`)
- Records all discovered IP and MAC addresses
- Saves logs to timestamped `.csv` files
- Optional USB copy support (in progress)
- View logs directly on-screen

---

## 📐 Project Structure

```plaintext
BAS-Brick/
├── bas_brick_launcher.py       # Main touchscreen launcher GUI
├── tools/
│   └── network_scanner/
│       ├── gui.py              # GUI for the network scanner
│       ├── scanner.py          # Core scanning logic (currently mocked)
│       └── config.json         # Subnet and IP configuration
├── shared/
│   └── utils.py                # Shared functions for future tools
├── assets/
│   └── bas_brick_logo.png      # (Optional) branding

---

## 🧰 Setup Instructions

1. **Install Raspberry Pi OS** (Lite or Full).
2. **Enable SPI, I2C, and SSH** via `raspi-config`.
3. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/BAS-Brick.git
   ```
4. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure static IP** (default is `10.46.12.2`) via `dhcpcd.conf`.

---

## 🖼️ Touchscreen Usage & Calibration

- The system is designed for a 3.5" GPIO touchscreen.
- Use `xinput_calibrator` for alignment if needed.
- Interface uses glove-friendly buttons and simple menus.

---

## 📸 Screenshots / UI Mockups

*Coming soon.*

---

## 🧭 Tool Roadmap

- ✅ Network Scanner
- ⏳ USB Log Exporter
- 🔜 BACnet MS/TP Discovery Tool
- 🔜 Modbus Sniffer
- 🔜 Wi-Fi Signal Mapper

---

## 🤝 Contributing

PRs welcome! For larger changes, open an issue to discuss first.
Use conventional commits and follow PEP8.

---

## ⚖️ License

MIT License. See `LICENSE` file for details.

---

## 🎯 Project Philosophy

**BAS-Brick** aims to:
- Empower BAS field professionals
- Prioritize usability and speed
- Be modular and extensible
- Work offline, in rugged environments
