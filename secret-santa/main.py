from data import participants
from generate_santas import generate_santas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from whatsapp_selenium import send_messages
import time


if __name__ == "__main__":
    santas_list = generate_santas(participants_list=participants)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    time.sleep(2)
    for santa in santas_list:
        send_messages(santa["phone"], santa["message"], driver)
        print(f"Sent message to {santa['giver']}")
    print("done")
