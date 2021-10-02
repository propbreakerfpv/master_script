# error handleing for master script
from colorama import init
from colorama import Fore, Back, Style


class Error():
    def __init__(self):
        init()
        pass

    def error(self, mesage, line):
        print(Fore.RED + "[ERROR]: " + Style.RESET_ALL + mesage + " on line: " + str(line))

if __name__ == "__main__":
    init()
    from colorama import Fore, Back, Style
    error = Error()
    error.error("invaled sintax")
    #print(Fore.RED + 'some red text')
    #print(Back.GREEN + 'and with a green background')
    #print(Style.DIM + 'and in dim text')
    #print(Style.RESET_ALL)
    #print('back to normal now')
