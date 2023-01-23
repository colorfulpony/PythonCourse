from bs4 import BeautifulSoup
from selenium import webdriver
import send_email
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.implicitly_wait(30)
    return driver

def clean_percentage(percentage):
    if "+" in percentage:
        percent = percentage.replace("+",'')
        percent = percent.split("%")[0]
    else:
        percent = percentage.split("%")[0]
    return float(percent)

def stock_price_notifier(ISIN):
    driver = get_driver()
    driver.get(f"https://zse.hr/en/indeks-366/365?isin={ISIN}&tab=index")
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    origin_percentage = soup.find('span', class_='stock-trend').get_text()
    percentage = clean_percentage(origin_percentage)
    if percentage < -0.10:
        send_email.send_notification()
    else:
        print(f"The percentage now is {percentage}")
    return


def main():
    ISIN = input("Enter ISIN nubmer:")

    stock_price_notifier(ISIN)

main()