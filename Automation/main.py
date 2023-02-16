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
    options.headless = True
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://search.sunbiz.org/Inquiry/CorporationSearch/ByName")
    return driver

# Connection To Worksheet
gc = gspread.service_account('secrets.json')
spreadsheet = gc.open('Copy of Landscaper - FL')
worksheet = spreadsheet.worksheet('HUB_20230205_(808)')

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


# Main Code
whileloop = True
cell_row = 2;
while whileloop:
    # Get driver instance
    driver = get_driver()

    # Cells Id
    company_name_cell_id = f'A{cell_row}'
    full_name_cell_id = f'B{cell_row}'
    first_name_cell_id = f'C{cell_row}'
    last_name_cell_id = f'D{cell_row}'

    # Get Company Name
    company_name = string_punctuation(worksheet.acell(company_name_cell_id).value.upper())

    #MAIN FUNCTION
    try:
        if check_exists("id", "SearchTerm"):
            # Get Search Input
            driver.find_element(
                by="id",
                value="SearchTerm"
            ).send_keys(company_name + Keys.RETURN)

            time.sleep(1)

            # Get First Company Name in List
            first_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/a"
            ).text)
            # Get Second Company Name in List
            second_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/a"
            ).text)
            # Get First Company Name Status in List
            first_corp_name_checker = driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]"
            ).text
            # Get Second Company Name Status in List
            second_corp_name_checker = driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[3]"
            ).text

            print(company_name,
                  "\n", first_company_name,
                  "\n", second_company_name,
                  "\n", first_corp_name_checker,
                  "\n", second_corp_name_checker)

            # Validation
            if company_name in first_company_name and first_corp_name_checker != "INACT" and first_corp_name_checker != "INACT/UA" and first_corp_name_checker != "INACT/CV" and first_corp_name_checker != "InActive":
                # Get First and Last Name of Owner
                driver.find_element(
                    by="xpath",
                    value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/a"
                ).click()

                time.sleep(0.2)

                full_name = driver.find_element(
                    by="xpath",
                    value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[5]/span[2]"
                ).text

                data = pd.DataFrame({"A": full_name.split()})

                print("\n" + full_name + "\n")
                print("Last Name =", data.iloc[0]['A'][:-1])
                print("First Name =", data.iloc[1]['A'])

                owner_last_name = data.iloc[0]['A'][:-1]
                owner_first_name = data.iloc[1]['A']

                # Update Worksheet
                worksheet.update(full_name_cell_id, full_name)
                worksheet.update(first_name_cell_id, owner_first_name)
                worksheet.update(last_name_cell_id, owner_last_name)

            elif company_name in second_company_name and second_corp_name_checker != "INACT" and second_corp_name_checker != "INACT/UA" and second_corp_name_checker != "INACT/CV" and second_corp_name_checker != "InActive":
                # Get First and Last Name of Owner
                driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/a").click()
                time.sleep(0.2)
                full_name = driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[5]/span[2]").text

                data = pd.DataFrame({"A": full_name.split()})
                print("\n" + full_name + "\n")
                print("Last Name =", data.iloc[0]['A'][:-1])
                print("First Name =", data.iloc[1]['A'])

                owner_last_name = data.iloc[0]['A'][:-1]
                owner_first_name = data.iloc[1]['A']

                # Update Worksheet
                worksheet.update(full_name_cell_id, full_name)
                worksheet.update(first_name_cell_id, owner_first_name)
                worksheet.update(last_name_cell_id, owner_last_name)
            else:
                worksheet.update(first_name_cell_id, '-')
                worksheet.update(last_name_cell_id, '-')
                print("THERE IS NO SUCH COMPANY NAME \n")
        else:
            print("Something went wrong \n")

        # Print that script works correctly
        print("UPDATED \n")
    except NoSuchElementException as ex:
        print("NO NEEDED ELEMENT\n" + ex.msg)

    # Update cell row
    cell_row += 1


