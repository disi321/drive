import os
import socket
import subprocess
import time
import requests
import threading

print("[+] Checking for internet connection")
res = ""
while "html" not in res and res is not None:
    try:
        res = requests.get("https://google.com/").text
    except Exception as e:
        pass
    time.sleep(1)

print("[+] Device is connected to the Internet\n")
ip_list = []
hmi = {}


def send_cmd(ip, port):
    print("Send malicious code")
    pass


def ip_exist(ip):
    global ip_list, hmi
    hmi_ports = (502, 44818)
    res = subprocess.run(["ping", ip], capture_output=True)
    if "Approximate round" in res.stdout.decode("UTF-8"):
        ip_list.append(ip)
        for port in hmi_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((ip, port))
            if result == 0:
                send_cmd(ip, port)
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