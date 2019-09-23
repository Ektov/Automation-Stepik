from my_func import *
import time

link = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()
driver.get(link)

driver.find_element_by_tag_name("button").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
x = driver.find_element_by_id("input_value").text
y = calc(int(x))
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_class_name("btn-primary").click()

time.sleep(10)

driver.close()







