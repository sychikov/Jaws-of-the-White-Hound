from Parser import get_links
from module_testing import main_test
import colorama
from colorama import Fore, Back, Style
import os

file_way = "testfile.txt"


def hello():

    try_clean = os.system("clear")
    colorama.init()
    print(Fore.RED + "\n⣿⣿⣿⡟⣹⣯⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⢿⣿⡟⢠⣿⣿⣿⣷⡌⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠸⣿⡇⢸⣿⣿⣿⣿⣿⡄⠄⢿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⡆⠹⡇⠄⣿⣿⣿⣿⣿⣿⡄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣷⡀⠄⠄⠘⣿⣿⣿⣿⣿⣿⡄⠄⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⢿⡆⠄⠄⠹⣿⣿⣿⣿⣿⣧⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣷⣦⣤⣀⠄⠘⢿⣿⣿⣿⣿⡆⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣷⣦⣄⠄⠄⠙⠿⣿⣿⡇⣀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣍⡀⠄⠄⠈⠛⢷⠋⠁⠉⠻⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣂⡀⠄⠄⠈⠄⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢶⣄⠄⠄⠸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢋⣠⣴⣾⡿⠄⠄⢰⣬⡙⠿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⠟⠁⠄⠄⠄⢿⣿⣷⣮⣾\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⢨⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⣸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣿⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")
    print("[  !!!  ] Jaws of the White Hound. Version 0.1.2.\n")
    main_cycle()

def help():
    print("[  +  ] HELP: \n")
    print("[  ?  ] help - show command list.")
    print("[  ?  ] exit - finish work.")
    print("[  ?  ] options - show list of options.")
    print("[  ?  ] change - change options. Syntax: change *option* *new value*.")
    print("[  ?  ] run - start testing.")

def options():
    print("[  ?  ] file_way: " + file_way)

def change_options(cmd_c):
    try:
        if cmd_c[1] == "file_way":
            file_way = cmd_c[3]
            print("[  +  ] file_way is changed. New value is: " + file_way + "\n")
        else:
            print("[  -  ] Invalid command. Try again. \n")
    except:
        print("[  -  ] Invalid syntax. Try again. \n")

def run():
    print("[  !  ] You feel like something terrible is coming. \n")
    Array = get_links(file_way)
    count = 0
    for link in Array:
        count += 1
        print("[  +  ] Test " + str(count) + "\n")
        main_test(link)

    print("[  +  ] " + str(count) + " tests is finished.\n")

def main_cycle():
    print("[  +  ] What is your orders? \n")
    cmd = input("[  \u261b  ] >>> ")

    while cmd != "exit":

        cmd_c = cmd.split(" ")

        if cmd_c[0] == "help":
            help()

        elif cmd_c[0] == "options":
            options()

        elif cmd_c[0] == "change":
            change_options(cmd_c)

        elif cmd_c[0] == "run":
            run()

        else:
            print("[  -  ] Invalid command. Try again. \n")
        cmd = input("\n[  \u261b  ] >>> ")


hello()
