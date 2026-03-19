import socket
import threading
from queue import Queue

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

# Common ports
common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 8000: "HTTP (Alt)", 8834: "Nessus"
}

# Queue for ports
queue = Queue()

# Fill queue
for port in range(1, 10001):
    queue.put(port)

# Scan function
def scan():
    while not queue.empty():
        port = queue.get()
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[OPEN] Port {port} - {service}")
        
        s.close()
        queue.task_done()

# Create threads
threads = []

for _ in range(100):  # number of threads
    t = threading.Thread(target=scan)
    t.start()
    threads.append(t)

# Wait for all threads
for t in threads:
    t.join()

print("\nScan complete.")
