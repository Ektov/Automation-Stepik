from selenium import webdriver
from math import *
from time import *

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(log(abs(12*sin(int(x)))))


x = int(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_id("robotCheckbox").click()
#browser.find_element_by_id("robotsRule").click()
#browser.execute_script("return argument.scrollIntoView(true);", radio)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element_by_id("robotsRule").click()
button.click()

time.sleep(10)

assert True