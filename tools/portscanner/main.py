"""
Author : No one cares
Github : You got it from there
"""

import sys
from colors import print_green, print_orange, print_red
from scanner import scan
from help import show_help


def main():
    args = sys.argv

    if len(args) >= 3:
        ip = None
        port = None
        scan_multiple_ports = False
        # scan(ip, port)
        for idx in range(0, len(args) - 1):
            option = args[idx]

            if option == "-ip":
                ip = args[idx + 1]
            if option == "-p":
                port = args[idx + 1]
            if option == "-ps":
                scan_multiple_ports = True
                port = args[idx + 1]
            else:
                continue

        if not ip or not port:
            show_help()
        else:
            scan(ip, port, scan_multiple_ports)

    else:
        show_help()


if __name__ == "__main__":
    main()
