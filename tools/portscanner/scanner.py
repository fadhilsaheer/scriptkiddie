import socket
from colors import print_green, print_red


def scan(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print_green(f"[+] {port} IS OPEN")
    except:
        print_red(f"[-] {port} IS CLOSE")
