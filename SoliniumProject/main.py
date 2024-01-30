from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
driver.maximize_window()
DateInwidget = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
DataInwidget = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")



events = {}

for i in range(len(DateInwidget)):
    events[i] = {
        'Time': DateInwidget[i].text,
        'Title': DataInwidget[i].text
    }

print(events)
