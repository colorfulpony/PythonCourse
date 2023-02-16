import gspread
import time
import pandas as pd
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import string


# Driver Connection
def get_driver():
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.dnb.com/site-search-results.html#CompanyProfilesPageNumber=1"
               "&CompanyProfilesSearch=""&ContactProfilesPageNumber=1&DAndBMarketplacePageNumber=1"
               "&DAndBMarketplaceSearch=""&IndustryPageNumber=1&SiteContentPageNumber=1"
               "&SiteContentSearch=""&tab=All")
    return driver


# Validate String Punctuation
def string_punctuation(s):
    whitelist = string.ascii_letters + string.digits + ' ' + "&" + "'" + "-"
    for char in string.punctuation:
        if char not in whitelist:
            s = s.replace(char, '')
    return s


# Check is Exists some Element
def check_exists(by, value):
    try:
        element = driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    return element


# Connection To Worksheet
gc = gspread.service_account('secrets.json')
spreadsheet = gc.open('Copy of Landscaper - FL')
worksheet = spreadsheet.worksheet('HUB_20230205_(808)')

while_loop = True
cell_row = 3
while while_loop:
    # Get driver instance
    driver = get_driver()

    # Cells Id
    company_name_cell_id = f'A{cell_row}'
    full_name_cell_id = f'B{cell_row}'
    first_name_cell_id = f'C{cell_row}'
    last_name_cell_id = f'D{cell_row}'

    # Get Company Name
    company_name = string_punctuation(worksheet.acell(company_name_cell_id).value.upper())

    # MAIN FUNCTION
    try:
        time.sleep(10)

        driver.find_element(
            by="xpath",
            value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div[1]/div/div/div/div[1]/input"
        ).send_keys(company_name)

        time.sleep(3)

        if check_exists("xpath", "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/a/div[1]"):
            first_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/a/div[1]"
            ).text.upper())

        if check_exists("xpath", "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a/div[1]"):
            second_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a/div[1]"
            ).text.upper())

        print(company_name,
              "\n", first_company_name,
              "\n", second_company_name)
        print (company_name in first_company_name, company_name in second_company_name)
        time.sleep(3)

        if company_name in first_company_name:
            if check_exists(
                "xpath",
                "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/a"
            ):
                driver.find_element(
                    by="xpath",
                    value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/a"
                ).click()

                time.sleep(10)

                # Get First and Last Name of Owner
                full_name = driver.find_element(
                    by="xpath",
                    value="/html/body/div[2]/div[3]/div/div/div[9]/div/div/div/div/div[2]/ul/li[1]/div[1]"
                ).text[5:]

                first_name = full_name.split()[0]
                last_name = full_name.split()[1]
                print("\n" + full_name + "\n")
                print("Last Name =", last_name)
                print("First Name =", first_name)

                # Update Worksheet
                worksheet.update(full_name_cell_id, full_name)
                worksheet.update(first_name_cell_id, first_name)
                worksheet.update(last_name_cell_id, last_name)

                # Print that script works correctly
                print("UPDATED \n")
            else:
                worksheet.update(first_name_cell_id, '-')
                worksheet.update(last_name_cell_id, '-')
                print("THERE IS NO SUCH COMPANY NAME \n")
        elif company_name in second_company_name:
            if check_exists(
                "xpath",
                "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a"
            ):
                driver.find_element(
                    by="xpath",
                    value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a"
                ).click()

                time.sleep(10)

                # Get First and Last Name of Owner
                full_name = driver.find_element(
                    by="xpath",
                    value="/html/body/div[2]/div[3]/div/div/div[9]/div/div/div/div/div[2]/ul/li[1]/div[1]"
                ).text[5:]

                first_name = full_name.split()[0]
                last_name = full_name.split()[1]
                print("\n" + full_name + "\n")
                print("Last Name =", last_name)
                print("First Name =", first_name)

                # Update Worksheet
                worksheet.update(full_name_cell_id, full_name)
                worksheet.update(first_name_cell_id, first_name)
                worksheet.update(last_name_cell_id, last_name)

                # Print that script works correctly
                print("UPDATED \n")
            else:
                worksheet.update(first_name_cell_id, '-')
                worksheet.update(last_name_cell_id, '-')
                print("THERE IS NO SUCH COMPANY NAME \n")
        else:
            worksheet.update(first_name_cell_id, '-')
            worksheet.update(last_name_cell_id, '-')
            print("THERE IS NO SUCH COMPANY NAME \n")
    except NoSuchElementException as ex:
        print("NO NEEDED ELEMENT\n" + ex.msg)

    # Update cell row
    cell_row += 1
