# Basic portscanner

import socket
import sys
from colors import print_green, print_orange, print_red

# Trying to connect with specified port


def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print_green(f"[+] {str(port)} IS OPENED")
        sock.close()
    except:
        print_red(f"[-] {str(port)} IS CLOSED")

# Help


def show_help():
    print("\nHELP\n")
    print_orange("usage: python3 portscanner.py <ip> <port>\n")


# Main function
def main():
    args = sys.argv

    if len(args) == 3:
        ip = args[1]
        port = args[2]
        scan_port(ip, int(port))

    else:
        show_help()


main()
