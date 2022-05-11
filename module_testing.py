from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
import pandas as pd
from module_parsing import white, white_borderless, crop_link, get_type_of_link
#from module_downloading import download

main_injection = '<script>alert("bGljayBteSBiYWxscw")</script>'
Array_of_results = []
site = None
primal_site = None
slave_site = None
iteration_level = 0
is_quick_test = 0
Array_of_links = None


def prnt_info(title, file_way):
    print("[  ?  ] Link of site:" + white(file_way))
    print("[  ?  ] Title of site:" + white(title))

def form_parser(is_quick_test):
    try:
        Array_of_form_tmp = site.find_elements_by_xpath("//form")
        if len(Array_of_form_tmp) == 0:
            print("[  -  ] There is no way to inject.")
            return 0

        Array_of_form = []
        for form in Array_of_form_tmp:
            if form.find_elements_by_xpath('.//input[@type="text"]'):
                Array_of_form.append(form)

        if is_quick_test == 1:
            print("[  ?  ] There is" + white(len(Array_of_form)) + "potential ways to attack.")

        return Array_of_form
    except:
        print("[  -  ] Something wrong with creating array of forms. \n")

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
    Array_of_form = form_parser(0)
    local_count = 0
    for form in Array_of_form:
        local_count +=1
        if local_count == count:
            Array_of_inputs = form.find_elements_by_xpath('.//input[@type="text"]')
            for inpt in Array_of_inputs:
                inpt.send_keys(main_injection)
            tmp = form.get_attribute("innerHTML")
            try:
                button = form.find_element_by_xpath('.//input[@type="button"]')
                button.click()
            except:
                form.send_keys(Keys.ENTER)
            if check_alerts():
                info_of_vulnerability(tmp)
            break


def info_of_vulnerability(info):
    print("[  ?  ] Vulnerable code: \n")
    print(white_borderless(info) + "\n")


def check_alerts():
    alert = Alert(site)
    if alert.text == "bGljayBteSBiYWxscw":
        print("[  !  ] Found the vulnerability !")
        alert.accept()
        return 1
    else:
        return 0


def main_test(file_way_t, iteration_level_tmp):
    #try:
        global iteration_level
        global Array_of_links
        file_way = file_way_t
        iteration_level = iteration_level_tmp

        #if get_type_of_link(file_way) != "file:":
            #file_way = download(file_way_t, iteration_level)

        site = prepare(file_way)
        site.implicitly_wait(10)
        prnt_info(site.title, file_way)
        Array_of_form = form_parser(1)
        prepare_slaves_and_primals(file_way)

        if iteration_level == 0:
            result = began_test(file_way, Array_of_form)

        else:
            part_of_href = crop_link(file_way)
            #Array_of_links = get_href(part_of_href)


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

