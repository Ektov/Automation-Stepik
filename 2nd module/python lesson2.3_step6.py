from selenium import webdriver
import time
import my_func

link = 'http://suninjuly.github.io/redirect_accept.html'
driver = webdriver.Chrome()
driver.get(link)

driver.find_element_by_class_name("trollface").click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
x = driver.find_element_by_id("input_value").text
y = my_func.calc(int(x))
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_class_name("btn-primary").click()

time.sleep(10)

driver.close()

#driver.switch_to.alert.accept()
#time.sleep(1)

