from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/home")


# cookie = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[15]/div[8]/button")
def SignUpOption():
    LoginOptionEmail = driver.find_element(By.XPATH,
                                           "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
    LoginOptionEmail.send_keys('alsojiblimon@gmail.com')
    LoginOptionUserPassword = driver.find_element(By.XPATH,
                                                  "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")
    LoginOptionUserPassword.send_keys('LimonLi34@')
    ButtonClick = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/button').click()


SignUpOption()

# EasyApplyButton = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button[aria-label="Easy Apply to Community Growth '
#                                                        'Manager - Telegram (Crypto) at KoinBasket"]button')
# EasyApplyButton.click()
#JoinNow = driver.find_element(By.LINK_TEXT, 'Join Now')
time.sleep(500)
