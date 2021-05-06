import socket
from colors import print_green, print_red, print_orange


def scan_port(ip, port, no_warnings):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print_green(f"[+] {port} IS OPEN")
    except:
        if no_warnings:
            return
        print_red(f"[-] {port} IS CLOSE")


def scan(ip, port, scan_multiple_ports, no_warnings):
    print_orange(f"[*] Scanning {str(ip)}")

    port = int(port)

    if scan_multiple_ports:
        for prt in range(1, port + 1):
            scan_port(ip, prt, no_warnings)
    else:
        scan_port(ip, port, no_warnings)
