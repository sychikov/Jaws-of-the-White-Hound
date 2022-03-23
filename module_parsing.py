import colorama
from colorama import Fore, Back, Style

def get_links(FileWay):
    try:
        with open(FileWay, "r") as File:
            ArrayOfLinks = []
            for link in File:
                link = link[:link.find('/n')]
                ArrayOfLinks.append(link)

            return ArrayOfLinks

    except:
        print("File reading error")

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
