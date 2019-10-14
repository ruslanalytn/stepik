from selenium import webdriver
import time 
import math
link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1")
    x = number1.text
    number2 = browser.find_element_by_id("num2")
    y = number2.text
    summa = str(int(x) + int(y))
    otvet = browser.find_element_by_id("dropdown").click()
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summa)
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
