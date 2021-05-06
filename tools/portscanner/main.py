# Basic portscanner

import sys
from colors import print_green, print_orange, print_red
from scanner import scan
from help import show_help


def main():
    args = sys.argv

    if len(args) == 3:
        ip = args[1]
        port = args[2]
        scan(ip, int(port))

    else:
        show_help()


if __name__ == "__main__":
    main()
