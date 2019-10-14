from selenium import webdriver
import time 
import math
import os
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("rus")
    lastname = browser.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("gun")
    robot = browser.find_element_by_xpath("//input[@placeholder='Enter email']").send_keys("ppp@mail.ru")
    viberite = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    viberite.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
