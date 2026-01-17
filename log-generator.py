#!/usr/bin/env python3
import random
import time
import json
from datetime import datetime
import socket
import sys

# Configuration
LOGSTASH_HOST = 'localhost'
LOGSTASH_PORT = 5000

# Simulated attack patterns
ATTACK_PATTERNS = [
    {
        "message": "Failed SSH login for user 'root' from {ip}",
        "level": "WARNING",
        "protocol": "SSH",
        "port": 22
    },
    {
        "message": "Port scan detected on ports 80,443,8080 from {ip}",
        "level": "HIGH",
        "protocol": "TCP",
        "port": 0
    },
    {
        "message": "SQL injection attempt in login form: ' OR '1'='1",
        "level": "CRITICAL", 
        "protocol": "HTTP",
        "port": 80
    },
    {
        "message": "Normal user login successful for admin@company.com",
        "level": "INFO",
        "protocol": "HTTP",
        "port": 443
    },
    {
        "message": "Firewall blocked connection from {ip} to port 3389",
        "level": "MEDIUM",
        "protocol": "RDP",
        "port": 3389
    },
    {
        "message": "DDoS attack detected - 1000 requests/second from {ip}",
        "level": "CRITICAL",
        "protocol": "HTTP",
        "port": 80
    },
    {
        "message": "System backup completed successfully",
        "level": "INFO", 
        "protocol": "SYSTEM",
        "port": 0
    }
]

# Fake IP addresses
FAKE_IPS = [
    "192.168.1.",  # Internal
    "10.0.0.",     # Internal
    "45.33.32.",   # External
    "185.159.82.", # External
    "94.23.152."   # External
]

def generate_ip():
    """Generate a random IP address"""
    network = random.choice(FAKE_IPS)
    return network + str(random.randint(1, 254))

def send_log(log_data):
    """Send log to Logstash via TCP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((LOGSTASH_HOST, LOGSTASH_PORT))
        sock.sendall((json.dumps(log_data) + '\n').encode())
        sock.close()
        return True
    except Exception as e:
        print(f"[!] Could not connect to Logstash: {e}")
        print(f"[*] Log saved locally instead")
        return False

def main():
    """Main log generation loop"""
    print("[*] SOC Log Generator Started")
    print("[*] Press Ctrl+C to stop\n")
    
    try:
        while True:
            # Pick a random attack pattern
            pattern = random.choice(ATTACK_PATTERNS)
            
            # Create log entry
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "level": pattern["level"],
                "message": pattern["message"].format(ip=generate_ip()),
                "source_ip": generate_ip(),
                "destination_ip": "192.168.1.1",
                "protocol": pattern["protocol"],
                "port": pattern["port"],
                "hostname": f"server-{random.randint(1, 10)}",
                "event_id": f"EVT-{random.randint(1000, 9999)}"
            }
            
            # Try to send to Logstash
            if not send_log(log_entry):
                # Save locally if Logstash is down
                with open("sample-logs/soc-events.log", "a") as f:
                    f.write(json.dumps(log_entry) + "\n")
            
            # Print to console
            print(f"[{log_entry['timestamp']}] {log_entry['level']}: {log_entry['message']}")
            
            # Random delay between logs (1-5 seconds)
            time.sleep(random.uniform(1, 5))
            
    except KeyboardInterrupt:
        print("\n[*] Stopping log generator...")
        sys.exit(0)

if __name__ == "__main__":
    # Install required packages if missing
    try:
        import socket
        import json
    except ImportError:
        print("[!] Required modules not found. Install with:")
        print("    sudo apt install python3-socket python3-json")
        sys.exit(1)
    
    main()
