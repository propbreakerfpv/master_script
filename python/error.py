# error handleing for master script
from colorama import init
from colorama import Fore, Back, Style


class Error():
    def __init__(self):
        init()
        pass

    def error(self, mesage, line):
        print(Fore.RED + "[ERROR]: " + Style.RESET_ALL + mesage + " on line: " + str(line))

    def worn(self, mesage, line):
        print(Fore.YELLOW + "[worning]: " + Style.RESET_ALL + mesage + " on line: " + str(line))

    def print(self, mesage):
        print(Fore.RED + mesage + Style.RESET_ALL)

if __name__ == "__main__":
    init()
    from colorama import Fore, Back, Style
    error = Error()
    error.error("invaled sintax")
