import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


def send_messages(phone_number: str, message_text: str, driver: WebDriver):
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    # Enter the target number in the target variable. Example 1234567890
    target = phone_number
    x_arg = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    time.sleep(10)
    group_title.click()
    group_title.send_keys(target + Keys.ENTER)
    inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(message_text + Keys.ENTER)
    time.sleep(4)
