# 🛡️ Honeypot-System

### SSH Honeypot Framework for Cybersecurity Research and Threat Analysis

A lightweight low-interaction SSH honeypot designed to simulate vulnerable services, collect attacker behavior, and support cybersecurity education, threat intelligence, and security research.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.x-green)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Overview

HeroHoneypot is a research-oriented SSH honeypot that emulates a vulnerable SSH service to attract unauthorized access attempts and record attacker behavior.

The framework captures authentication attempts, shell commands, source IP information, and geolocation data to help researchers, students, and security professionals study real-world attack patterns in controlled environments.

The project is intended for cybersecurity learning, defensive security research, and threat analysis.

---

## 🚀 Key Features

### Attack Simulation

* Low-Interaction SSH Honeypot
* Simulated Login Environment
* Configurable Credentials
* Realistic Session Behavior

### Threat Intelligence Collection

* Credential Harvest Logging
* Command Execution Tracking
* Source IP Monitoring
* Session Recording
* Timestamped Event Collection

### Geolocation Analysis

* GeoIP Integration
* Country Identification
* City-Level Approximation
* Attack Source Mapping

### Analytics & Visualization

* Top Attacker IP Analysis
* Most Common Commands
* Attack Trend Visualization
* Session Activity Reports

---

## 📂 Project Structure

```text
honeypot-system/

├── README.md
├── requirements.txt
├── config.yaml
│
├── src/
│   ├── honeypot.py
│   ├── logger.py
│   └── visualizer.py
│
└── logs/
    └── session_logs.json
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/honeypot-system.git

cd honeypot-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### GeoIP Database

Create a free account at MaxMind and download the GeoLite2 City database.

Place the downloaded database file in the project root directory before running the honeypot.

### Configuration

Edit the configuration file:

```yaml
host: "0.0.0.0"
port: 2222
username: "admin"
password: "1234"
```

### Start Honeypot

```bash
python src/honeypot.py
```

---

## 📊 Attack Visualization

Generate analytical reports and charts using:

```bash
python src/visualizer.py
```

### Available Insights

* Top Attacker IP Addresses
* Most Frequently Executed Commands
* Session Activity Trends
* Geographic Attack Distribution

---

## 📄 Sample Log Format

```json
{
  "timestamp": "2025-08-15T12:34:56",
  "ip": "192.168.1.101",
  "username": "admin",
  "password": "1234",
  "command": "ls -la",
  "location": {
    "city": "New York",
    "country": "United States"
  }
}
```

---

## 🎯 Use Cases

* Cybersecurity Education
* Security Awareness Training
* Threat Intelligence Research
* Attack Pattern Analysis
* Defensive Security Testing
* Academic Research
* Laboratory Environments

---

## 🔮 Roadmap

### Version 2.x

* Real-Time Attack Notifications
* Telegram Alert Integration
* Discord Alert Integration
* Slack Notifications

### Version 3.x

* Web-Based Monitoring Dashboard
* Interactive Analytics
* Session Playback
* Multi-Honeypot Management

### Version 4.x

* Threat Intelligence Export
* IOC Generation
* SIEM Integration
* Advanced Reporting

### Version 5.x

* Multi-Protocol Support
* FTP Honeypot
* HTTP Honeypot
* Telnet Honeypot
* SMB Honeypot

---

## ⚠️ Disclaimer

HeroHoneypot is intended exclusively for educational purposes, cybersecurity research, laboratory environments, threat intelligence collection, and authorized security testing.

The software should only be deployed in environments where monitoring and data collection activities are permitted and compliant with applicable laws and regulations.

Users are solely responsible for ensuring legal and ethical use of the software.

The author is not responsible for misuse, unauthorized deployment, or illegal activities conducted using this project.

---

## 👨‍💻 Creator

### Shibnath Hansda

Founder of HansdaTechs

Cybersecurity Enthusiast • Security Researcher • Open Source Developer

### Connect

[![GitHub](https://img.shields.io/badge/GitHub-Hero24--x-181717?style=for-the-badge&logo=github)](https://github.com/Hero24-x)

[![Instagram](https://img.shields.io/badge/Instagram-@ethicalhansda-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/ethicalhansda)

[![Email](https://img.shields.io/badge/Email-hansdatechs24@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hansdatechs24@gmail.com)

---

## 📜 License

Released under the MIT License.

---

## Honeypot-System

### Observe Threats • Study Attackers • Strengthen Defenses

Built with ❤️ by Shibnath Hansda
