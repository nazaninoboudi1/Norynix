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
git clone https://github.com/nazaninoboudi1/Norynix.git
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

