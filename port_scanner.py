import socket
import subprocess
from datetime import datetime

target = input("Enter the target IP address: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"Scanning the target {ip}......")
        print("Time started: ", datetime.now())

        for port in range(22,81):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            s.close()
    
    except socket.gaierror:
        print("Hostname could not be resolved!")
    
    except socket.error:
        print("Could not connect to the server!")

port_scan(target)