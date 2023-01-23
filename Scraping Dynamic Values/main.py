from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    driver.get("https://www.timeanddate.com/worldclock/ukraine/kyiv")
    return driver

def get_hours(time):
    hour = float(time.split(":")[0])
    return hour

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[5]/main/article/section[1]/div[1]/div/span[1]")
    return get_hours(element.text)

print(main())