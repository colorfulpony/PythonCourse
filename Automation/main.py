import gspread
import time
import pandas as pd
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

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
spreadsheet = gc.open('Copy of Accountant - Florida ')
worksheet = spreadsheet.worksheet('HUB_20230127_(3781)')

def check_exists(by, value):
    try:
        element = driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    return element

# Main Code
whileloop = True
cell_row = 1954;
while whileloop:
    # Get driver instance
    driver = get_driver()

    # Cells Id
    company_name_cell_id = f'A{cell_row}'
    full_name_cell_id = f'B{cell_row}'
    first_name_cell_id = f'C{cell_row}'
    last_name_cell_id = f'D{cell_row}'

    #Get Company Name
    company_name = worksheet.acell(company_name_cell_id).value

    # Get owner page
    try:
        if check_exists("id", "SearchTerm"):
            driver.find_element(by="id", value="SearchTerm").send_keys(company_name)
            if check_exists("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/form/div[2]/div[2]/input"):
                driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div[2]/div/div/form/div[2]/div[2]/input").click()
                if check_exists("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]"):
                    corp_name_checker = driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]").text

                    # Get First and Last Name of Owner
                    if corp_name_checker != "INACT":
                        driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/a").click()
                        time.sleep(0.2)
                        full_name = driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[5]/span[2]").text

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
                    worksheet.update(first_name_cell_id, '-')
                    worksheet.update(last_name_cell_id, '-')
                    print("THERE IS NO SUCH COMPANY NAME \n")
            else:
                worksheet.update(first_name_cell_id, '-')
                worksheet.update(last_name_cell_id, '-')
                print("THERE IS NO SUCH COMPANY NAME \n")
    except:
        worksheet.update(first_name_cell_id, '-')
        worksheet.update(last_name_cell_id, '-')
        print("THERE IS NO SUCH COMPANY NAME \n")


    # Update cell row
    cell_row += 1

    # Print that script works correctly
    print("UPDATED \n")


