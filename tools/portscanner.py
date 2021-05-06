# Basic portscanner

import socket
import sys
from colorama import init, Fore

# Colors
init(autoreset=True)


def print_red(statement):
    print(Fore.RED + statement)


def print_green(statement):
    print(Fore.GREEN + statement)


def print_orange(statement):
    print(Fore.YELLOW + statement)

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
        scan_port(ip, port)

    else:
        show_help()


main()
