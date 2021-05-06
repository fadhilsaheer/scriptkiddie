from colors import print_orange


def show_help():
    print("\nHELP\n")
    print_orange("usage: python3 portscanner.py <options>\n")
    print("\nOPTIONS\n")
    print("-ip <target-ip>")
    print("-p <target-port>\n")

    print_orange("-nw : No warnings")
    print_orange("-ps <number> : scan a range of ports\n")
