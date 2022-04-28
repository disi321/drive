import subprocess
import threading
import time
import socket
import random

hmi_ports = (502, 44818, 443)

def clear_file():
    with open("./hmi_list.txt", "w") as f:
        f.write("")

#write to file
def write_to_file(ip, port):
    with open("./hmi_list.txt", "a") as f:
        f.write(f"{ip, port}\n")

# read list from file
def read_from_file():
    l = []
    with open("./ip_list.txt", "r") as f:
        for line in f:
            ip = line.strip()
            l.append(ip)
    return l

def is_hmi(ip):
    for port in hmi_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Found HMI in {ip}:{port}")
            write_to_file(ip, port)
            

def scan_for_hmi():
    clear_file()
    for ip in read_from_file():
        print(f"Checking --> {ip}")
        while threading.active_count() > 400:
            pass
        threading.Thread(target=is_hmi, args=[ip]).start()

scan_for_hmi()

