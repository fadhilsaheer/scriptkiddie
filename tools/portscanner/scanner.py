import socket
from colors import print_green, print_red


def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print_green(f"[+] {port} IS OPEN")
    except:
        print_red(f"[-] {port} IS CLOSE")


def scan(ip, port, scan_multiple_ports):
    port = int(port)
    if scan_multiple_ports:
        for prt in range(1, port):
            scan_port(ip, prt)
    else:
        scan_port(ip, port)
