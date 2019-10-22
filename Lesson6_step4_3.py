from selenium import webdriver
import time
import math

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Учеба/Сафаров/Python/chromedriver.exe')
    browser.get(link)


    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("I")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("P")
    input3 = browser.find_element_by_name('firstname')
    input3.send_keys("S")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("R")

    button = browser.find_element_by_css_selector('div>button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла