# Norynix

# ⚡ Norynix

🔍 A modular reconnaissance and penetration testing automation framework designed to reduce repetitive tasks during the early stages of security assessments.

> 🚧 Project Status: Early Development (v0.2)

---

## ✨ Features

### Current

- DNS Enumeration
  - A Records
  - AAAA Records
  - MX Records
  - NS Records

- Subdomain Enumeration
  - Common subdomain discovery
  - DNS resolution

### Planned

- HTTP Probing
- Technology Detection
- Port Discovery
- JSON Reporting
- Threaded Scanning
- Plugin System
- Recon Pipelines

---

## 🚀 Installation

```bash
git clone git@github.com:nazaninoboudi1/Norynix.git
cd Norynix

python3 -m venv venv
source venv/bin/activate

pip install -e .
pip install dnspython
```

---

## 🛠 Usage

```bash
norynix -s example.com
```

---

## 📂 Project Structure

```text
norynix/
├── cli.py
├── core/
│   └── runner.py
└── modules/
    └── subdomains.py
```

---

## 🗺 Roadmap

### v0.3
- Threaded scanning
- HTTP probing

### v0.4
- Technology fingerprinting
- JSON export

### v0.5
- Plugin architecture

---

## ⚠️ Disclaimer

This tool is intended for authorized security testing and educational purposes only.

Always obtain proper permission before scanning any target.

---

## 📜 License

MIT License
