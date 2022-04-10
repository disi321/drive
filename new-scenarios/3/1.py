# check internet connrection 
import requests
import time
def check():
    res = ""
    print("[+] Checking for internet connection")
    while "html" not in res and res is not None:
        try:
            res = requests.get("https://google.com/").text
        except Exception as e:
            print("[-] Device is not connected to the Internet\n")
        time.sleep(1)
    print("[+] Device is connected to the Internet\n")

check()