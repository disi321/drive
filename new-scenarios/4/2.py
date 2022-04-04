# read list from file
def read_from_file():
    l = []
    with open("./open_ports.txt", "r") as f:
        for line in f:
            ip = line.split("/")[0]
            l.append(ip)
    return l

def clear_file():
    with open("./hmi_list.txt", "w") as f:
        f.write("")

def write_to_file(ip, port):
    with open("./hmi_list.txt", "a") as f:
        f.write(f"{ip, port}\n")

def which_ami():
    print("[+] find type of HMI")
    ports = read_from_file()
    if :#to complite
        # handle one hmi
    else:
        # handle other hmi
    print("[+] find HMI type")
    clear_file()
    write_to_file(ip, port) # ALSO see



which_ami()