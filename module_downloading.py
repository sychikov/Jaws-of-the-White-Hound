import os
from datetime import date
import datetime

def download(file_way, iteration_level, count, main_folder):
    way = make_a_folder(count, main_folder)
    if iteration_level == 0:
        try_load = os.system("wget -k -E -U Mozilla -P " + way + " " + file_way)
    else:
        try_load = os.system("wget -k -l " + str(iteration_level) + " -E -U Mozilla -P "+ way + " " + file_way)

    abspath = "file://" + str(os.getcwd()) + way[1:] + "/index.html"
    return abspath

def make_main_folder():
    dt = str(datetime.datetime.now())
    dt = dt.split(" ")
    name = dt[0]
    dt = dt[1].split(":")
    final = float(dt[0])*60*60 + float(dt[1])*60 + float(dt[2])
    name = name + "-" + str(final)
    os.mkdir("./test_cases/" + name)
    return name

def make_a_folder(count, main_folder):
    name = "Test_" + str(count)
    way = "./test_cases/" + main_folder + "/"+name
    os.mkdir(way)
    return way
