from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

def click_the_button(var):
    button = driver.find_element(By.CLASS_NAME, var)
    button.click()

driver_path = "D:/downloads/chromeDriver/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

driver.get("https://github.com/")
driver.maximize_window()
time.sleep(1)
click_the_button("HeaderMenu-link--sign-in")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "js-login-field").send_keys("Mourad-Ouerghi")
driver.find_element(By.CLASS_NAME, "js-password-field").send_keys("1202-ellak")
click_the_button("js-sign-in-button")
time.sleep(2)
click_the_button("btn-primary")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "js-repo-name").send_keys(sys.argv[1])
click_the_button("btn-primary")