from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  

driver_path = "D:/downloads/chromeDriver/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

driver.get("https://github.com/")
driver.maximize_window()
time.sleep(1)
button = driver.find_element(By.CLASS_NAME, "HeaderMenu-link--sign-in")
button.click()