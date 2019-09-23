from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector(".btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

