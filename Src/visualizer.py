import json
import matplotlib.pyplot as plt
from collections import Counter

with open("logs/session_logs.json", "r") as f:
    logs = json.load(f)

ips = [log["ip"] for log in logs]
commands = [log["command"] for log in logs if log["command"]]

# Top IPs
ip_counts = Counter(ips).most_common(5)
labels, values = zip(*ip_counts)
plt.bar(labels, values)
plt.title("Top Attacker IPs")
plt.show()

# Top Commands
cmd_counts = Counter(commands).most_common(5)
labels, values = zip(*cmd_counts)
plt.bar(labels, values)
plt.title("Most Used Commands")
plt.show()
