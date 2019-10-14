from selenium import webdriver
import time 
import math
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_css_selector("span[id='input_value']")
    x = x_element.text
    y = calc(x)
    vvod = browser.find_element_by_id("answer")
    vvod.send_keys (y)
    robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot.click()
    browser.execute_script("window.scrollBy(0, 100);")
    robotrule = browser.find_element_by_css_selector("[value='robots']")
    robotrule.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
