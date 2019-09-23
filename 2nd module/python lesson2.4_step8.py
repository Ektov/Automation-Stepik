from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import my_func

link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(link)

button = driver.find_element_by_id("book")
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()
#if price:


x = driver.find_element_by_id("input_value").text
y = my_func.calc(int(x))
driver.find_element_by_id("answer").send_keys(y)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "solve"))).click()

#time.sleep(10)

#driver.close()