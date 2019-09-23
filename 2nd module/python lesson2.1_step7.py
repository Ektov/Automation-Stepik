from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x = browser.find_element_by_tag_name("img").get_attribute("valuex")
    #x_value = x.get_attribute("valuex")
    print(x)
    #y = calc(x)
    input1 = browser.find_element_by_id("answer").send_keys(calc(x))
    #input1.send_keys(y)

    for selector in ["#robotCheckbox", "#robotsRule", ".btn"]:
        browser.find_element_by_css_selector(selector).click()

    #checkbox = browser.find_element_by_id("robotCheckbox")
    #checkbox.click()
    #radio = browser.find_element_by_id("robotsRule")
    #radio.click()
    #button = browser.find_element_by_css_selector(".btn")
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()