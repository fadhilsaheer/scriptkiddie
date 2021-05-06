# Basic portscanner

import sys
from colors import print_green, print_orange, print_red
from scanner import scan


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
        scan(ip, int(port))

    else:
        show_help()


main()
