import colorama
from colorama import Fore, Back, Style
from module_downloading import download
from module_downloading import make_main_folder

main_folder = "111"

def get_links(FileWay, iteration_level):
    global main_folder
    #try:
    with open(FileWay, "r") as File:
        ArrayOfLinks = []
        count = 0
        for link in File:
            if check_for_download(link) == 0:
                link = link[:link.find('/n')]
                ArrayOfLinks.append(link)
            else:
                if main_folder == "111":
                    main_folder = make_main_folder()
                link = download(link, iteration_level, count, main_folder)
                ArrayOfLinks.append(link)
            count = count + 1

        return ArrayOfLinks

    #except:
        #print("Links reading error")

def check_for_download(link):
    part_of_link = link[:link.find(':')]
    if part_of_link == "file":
        return 0
    else:
        return 1

def white(strr):
    return Fore.WHITE + " " + str(strr) + " " + Fore.RED

def white_borderless(strr):
    return Fore.WHITE + str(strr) + Fore.RED

def crop_link(link):
    link_t = link.split("/")
    for str_tmp in link_t:
        if "." in str_tmp:
            return str_tmp

def get_type_of_link(link):
    link_t = link.split("/")
    return link_t[0]
