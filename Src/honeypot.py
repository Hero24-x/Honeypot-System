import socket
import threading
import yaml
import geoip2.database
from logger import log_event

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

HOST = config["honeypot"]["host"]
PORT = config["honeypot"]["port"]
USERNAME = config["honeypot"]["username"]
PASSWORD = config["honeypot"]["password"]

geo_reader = geoip2.database.Reader(config["geoip"]["database"])

def get_location(ip):
    try:
        response = geo_reader.city(ip)
        return {
            "city": response.city.name,
            "country": response.country.name
        }
    except:
        return None

def handle_client(conn, addr):
    ip = addr[0]
    conn.send(b"Username: ")
    username = conn.recv(1024).strip().decode()
    conn.send(b"Password: ")
    password = conn.recv(1024).strip().decode()

    location = get_location(ip)
    log_event(ip, username, password, location=location)

    if username == USERNAME and password == PASSWORD:
        conn.send(b"Welcome to fake shell!\n")
        while True:
            conn.send(b"$ ")
            cmd = conn.recv(1024).strip().decode()
            if cmd.lower() in ["exit", "quit"]:
                break
            log_event(ip, username, password, command=cmd, location=location)
            conn.send(b"Command not found\n")
    else:
        conn.send(b"Access Denied\n")

    conn.close()

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Honeypot running on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_honeypot()
  
