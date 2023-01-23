from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\\Users\\flexy\\OneDrive\\Рабочий стол\\PythonCourse\\TestProject.chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://ktc.ua/?_ac=gb&gclid=Cj0KCQiA_bieBhDSARIsADU4zLfDnRk-9lpRgAt61Jrk2SelxC6Ci0Txz86UbU5YwqTwud9oV6TO4xgaAuBZEALw_wcB")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div/div[3]/a[1]").click()
    time.sleep(2)
    driver.find_element(by="id", value="auth_login").send_keys("0971328349")
    time.sleep(2)
    driver.find_element(by="name", value="password").send_keys("Mak7ka321" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[1]/div[4]/footer/div/div[2]/div[2]/ul/li[1]/a").click()
    time.sleep(10)

print(main())