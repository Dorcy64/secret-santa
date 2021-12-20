from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service(executable_path='/Users/dorcy/Developer/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()


def send_messages(phone_number, message_text):
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    # Enter the target number in the target variable. Example 1234567890
    string = "Testing whatsapp automation python"
    target = phone_number
    x_arg = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    time.sleep(10)
    group_title.click()
    group_title.send_keys(target + Keys.ENTER)
    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(message_text + Keys.ENTER)
    time.sleep(4)
