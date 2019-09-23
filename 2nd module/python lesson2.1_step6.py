from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
#assert people_checked is not None, "People radio is not selected by default"
assert people_checked == "true", "People radio is not selected by default"
print("value of people radio: ", people_checked)
robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
print("value of robot radio: ", robots_checked)