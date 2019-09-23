from selenium import webdriver
import time

try:

    #link = "http://suninjuly.github.io/registration1.html"
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Sergey")
    input1 = browser.find_element_by_css_selector(".first_block .second")
    input1.send_keys("Ektov")
    input1 = browser.find_element_by_css_selector(".first_block .third")
    input1.send_keys("ek@123.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    assert isinstance(welcome_text_elt.text, object)
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text, 'Не равно'

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

