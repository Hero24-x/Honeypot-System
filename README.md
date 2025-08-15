# 🛡 Honeypot System by Hero

A **low-interaction SSH honeypot** developed by **Hero**, designed for research and educational purposes.  
It simulates a vulnerable SSH service, logs attacker activity (IP, credentials, commands), and visualizes intrusion attempts.

---

## 📌 Features
- **Fake SSH Login** – Attracts attackers with default/weak credentials.
- **Credential Logging** – Stores attempted usernames and passwords.
- **Command Tracking** – Captures every shell command entered by the attacker.
- **GeoIP Lookup** – Identifies the attacker’s approximate location.
- **Attack Visualization** – Charts for top IPs and frequently used commands.
- **Sample Logs** – Includes anonymized attack data for testing.

---

## ⚠ Disclaimer
> This project is created for **educational and research purposes only**.  
> Do **NOT** expose it to the public internet without proper authorization.  
> **Hero** is not responsible for any misuse or illegal activity.

---

## 📂 Project Structure
honeypot-system/
│
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── config.yaml # Configuration file
├── src/
│ ├── honeypot.py # Main honeypot server script
│ ├── logger.py # Event logging module
│ ├── visualizer.py # Attack visualization tool
│
└── logs/
└── session_logs.json # Stored attacker logs

--
## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/honeypot-system.git
cd honeypot-system

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Download GeoLite2 Database

Create a free MaxMind account and download GeoLite2-City.mmdb from:
https://dev.maxmind.com/geoip/geolite2-free-geolocation-data
Place it in the project root folder.

### 4️⃣ Configure settings

Edit config.yaml:

host: "0.0.0.0"
port: 2222
username: "admin"
password: "1234"

### 5️⃣ Run the honeypot
python src/honeypot.py

### 📊 Visualizing Attacks
python src/visualizer.py

Example graphs:
•Top Attacker IPs
•Most Used Commands

### 📜 Sample Log Format.
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

### 🔮 Future Improvements

Real-time attack alerts (Telegram/Slack).
Automatic IP blocking for detected malicious sources.
Web-based dashboard for live monitoring 

### 👨‍💻 Author
Shibnath Hansda – Cybersecurity Enthusiast & Developer
💼 hansdatechs24@gmail.com
