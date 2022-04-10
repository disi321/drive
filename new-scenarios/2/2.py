import subprocess
import threading
import socket

ip_list = []

#clear file
def clear_file():
    with open("./ip_list.txt", "w") as f:
        f.write("")

#write to file
def write_to_file(ip):
    with open("./ip_list.txt", "a") as f:
        f.write(f"{ip}\n")


def ip_exist(ip):
    global ip_list, hmi
    hmi_ports = (502, 44818, 443)
    res = subprocess.run(['ping', '-c', '1', ip], capture_output=True)
    if "from" in res.stdout.decode("UTF-8"):
        ip_list.append(ip)
        print(f"IP --> {ip}")
        write_to_file(ip)

def ipscanning():
    clear_file()
    print("file")
    global ip_list, hmi
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    local_ip = s.getsockname()[0]
    build_ip = local_ip.split(".")
    builder = f"{build_ip[0]}.{build_ip[1]}.{build_ip[2]}"
    print(f"[+] Local IP --> {local_ip}")
    print(f"[+] Scanning ip --> {builder}.x\n ")

    for class_d in range(1, 255):
        ip = f"{builder}.{class_d}"

        while threading.active_count() > 400:
            pass
        threading.Thread(target=ip_exist, args=[ip]).start()

ipscanning()