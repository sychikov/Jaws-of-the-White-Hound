from module_parsing import get_links, white, white_borderless
from module_testing import main_test
import colorama
from colorama import Fore, Back, Style
import os

file_way = "testfile.txt"
upload_links_from_file = 1
iteration_level = 0


def hello():
    try_clean = os.system("clear")
    colorama.init()
    print(Fore.RED + "\n⣿⣿⣿⡟⣹⣯⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⢿⣿⡟⢠⣿⣿⣿⣷⡌⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠸⣿⡇⢸⣿⣿⣿⣿⣿⡄⠄⢿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⡆⠹⡇⠄⣿⣿⣿⣿⣿⣿⡄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣷⡀⠄⠄⠘⣿⣿⣿⣿⣿⣿⡄⠄⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⢿⡆⠄⠄⠹⣿⣿⣿⣿⣿⣧⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣷⣦⣤⣀⠄⠘⢿⣿⣿⣿⣿⡆⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣷⣦⣄⠄⠄⠙⠿⣿⣿⡇⣀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣍⡀⠄⠄⠈⠛⢷⠋⠁⠉⠻⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣂⡀⠄⠄⠈⠄⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢶⣄⠄⠄⠸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢋⣠⣴⣾⡿⠄⠄⢰⣬⡙⠿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⠟⠁⠄⠄⠄⢿⣿⣷⣮⣾\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⢨⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⣸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣿⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")
    print("[  !!!  ] " + white_borderless("Jaws of the White Hound") + ". Version 0.1.4.\n")
    main_cycle()

def help():
    print("[  +  ] HELP: \n")
    print("[  ?  ]" + white("help") + "- show command list.")
    print("[  ?  ]" + white("exit") + "- finish work.")
    print("[  ?  ]" + white("options") + "- show list of options.")
    print("[  ?  ]" + white("change") + "- change options. Syntax: change *option* *new value*.")
    print("[  ?  ]" + white("run") + "- start testing.")

def options():
    print("[  ?  ] file_way: "+ white(file_way))
    print("[  ?  ] upload_links_from_file: "+ white(upload_links_from_file))
    print("[  ?  ] iteration_level: "+ white(iteration_level))

def change_options(cmd_c):
    global file_way
    global upload_links_from_file
    try:
        if cmd_c[1] == "file_way":
            file_way = cmd_c[2]
            print("[  +  ] file_way has been changed. New value is: " + file_way + "\n")

        elif cmd_c[1] == "upload_links_from_file":
            upload_links_from_file = cmd_c[2]
            print("[  +  ] upload_links_from_file has been changed. New value is: " + str(upload_links_from_file) + "\n")

        elif cmd_c[1] == "iteration_level":
            iteration_level = cmd_c[2]
            print("[  +  ] iteration_level has been changed. New value is: " + str(iteration_level) + "\n")
            print("[  !  ] Warning! By changing this option, you can spawn much more processes than your machine can handle.\n")

        else:
            print("[  -  ] Invalid command. Try again. \n")
    except:
        print("[  -  ] Invalid syntax. Try again. \n")

def run():
    #try:
        print("[  !  ] You feel like something terrible is coming. \n")
        if upload_links_from_file == 1:
            Array = get_links(file_way)
            count = 0
            for link in Array:
                count += 1
                print("[  +  ] Test " + str(count) + "\n")
                main_test(link, iteration_level)
        else:
            print("[  !  ] What is the link of your site?\n")
            link = input("[  \u261b  ] >>> ")
            main_test(link, iteration_level)

        print("[  +  ]" + white(count) + "tests is finished.\n")

    #except:
        #print("[  -  ] Something wrong with links. Try again. \n")

def main_cycle():
    print("[  +  ] What is your orders? \n")
    cmd = input("[  \u261b  ] >>> " + Fore.WHITE)
    print(Fore.RED)
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
            print("[  ?  ] Command 'help' can be useful. Sometimes. \n")

        cmd = input("\n[  \u261b  ] >>> " + Fore.WHITE)
        print(Fore.RED)


hello()
