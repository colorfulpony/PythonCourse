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
    driver.get("https://dribbble.com/session/new")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="login").send_keys("flexywall@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys("mak7ka321" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[5]/div[1]/div[1]/div[2]/ul/li[2]/a")

    return element.text


print(main())