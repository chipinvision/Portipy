#!usr/bin/python3
#Portipy - a nmap based network and port scanner made with python

# IMPORTING MODULES
import socket #pip3 install socket
import pyfiglet #pip3 install pyfiglet
import time

# COLOR CLASS
class colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    PROMPT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# BANNER
banner = pyfiglet.figlet_format("portipy", font="5lineoblique")
print(colors.GREEN + banner + colors.ENDC)
print(colors.FAIL + '-------------- Created by invisionchip --------------' + colors.ENDC)
print('\n')

# MAIN TOOL
print(colors.CYAN + '[+] Simple Port Scan Started...' + colors.ENDC)
host = str(input(colors.PROMPT + "[*] Enter the host to be scanned:" + colors.ENDC))
ip = socket.gethostbyname(host)
print(ip)
while 1:
    port_no = int(input(colors.PROMPT + "[*] Enter Port Number:" + colors.ENDC))
    try:
        sock = socket.socket()
        result = sock.connect(ip, host)
        print(colors.GREEN + "Port {}: Open".format(port_no) + colors.ENDC)
        sock.close()
    except:
        print(colors.FAIL + "Port {}: Closed".format(port_no) + colors.ENDC)
print(colors.GREEN + "[+] Port Scanning Completed..." + colors.ENDC)