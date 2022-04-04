import os
ip = #todo
os.system(f"nmap {ip} | grep open > open_ports.txt")