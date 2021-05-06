from colorama import Fore, init

init(autoreset=True)


def print_red(statement):
    print(Fore.RED + statement)


def print_green(statement):
    print(Fore.GREEN + statement)


def print_orange(statement):
    print(Fore.YELLOW + statement)
