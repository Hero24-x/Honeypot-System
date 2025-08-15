import json
from datetime import datetime

def log_event(ip, username, password, command=None, location=None):
    log_file = "logs/session_logs.json"
    
    try:
        with open(log_file, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    event = {
        "timestamp": datetime.now().isoformat(),
        "ip": ip,
        "username": username,
        "password": password,
        "command": command,
        "location": location
    }

    logs.append(event)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)
      
