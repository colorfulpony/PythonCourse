import time
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import string
from selenium import webdriver


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
def check_exists(by, value, driver):
    try:
        element = driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    return element


def get_company_owner_by_bnd(company_name):
    # Get driver instance
    driver = get_driver()

    # MAIN FUNCTION
    try:
        # Init names
        first_company_name = None
        second_company_name  = None

        time.sleep(10)

        driver.find_element(
            by="xpath",
            value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div[1]/div/div/div/div[1]/input"
        ).send_keys(company_name)

        time.sleep(3)
        if driver.find_element(
            by="xpath",
            value="/html/body/div[1]/div[3]/div[1]/div/"
                  "div/div[3]/div/div/div/div/div[2]/div/div[1]/a/div[1]"
        ):

            first_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[3]/div[1]/div/"
                      "div/div[3]/div/div/div/div/div[2]/div/div[1]/a/div[1]"
            ).text.upper())
        if driver.find_element(
            by="xpath",
            value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div"
                  "/div/div/div/div[2]/div/div[2]/a/div[1]"
        ):
            second_company_name = string_punctuation(driver.find_element(
                by="xpath",
                value="/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div"
                      "/div/div/div/div[2]/div/div[2]/a/div[1]"
            ).text.upper())

        print(company_name,
              "\n", first_company_name,
              "\n", second_company_name)
        print(company_name in first_company_name, company_name in second_company_name)
        time.sleep(3)

        if company_name in first_company_name:
            if check_exists(
                "xpath",
                "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/a",
                driver
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

                owner_first_name = full_name.split()[0]
                owner_last_name = full_name.split()[1]
                print("\n" + full_name + "\n")
                print("Last Name =", owner_last_name)
                print("First Name =", owner_first_name)

                return full_name, owner_first_name, owner_last_name

            else:
                print("Something went wrong\n")
                return False
        elif company_name in second_company_name:
            if check_exists(
                "xpath",
                "/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a",
                driver
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

                owner_first_name = full_name.split()[0]
                owner_last_name = full_name.split()[1]
                print("\n" + full_name + "\n")
                print("Last Name =", owner_last_name)
                print("First Name =", owner_first_name)

                return full_name, owner_first_name, owner_last_name
            else:
                print("Something went wrong \n")
                return False
        else:
            print("dnb has no such company \n")
            return None
    except NoSuchElementException as ex:
        print("Something went wrong\n" + ex.msg)
        return False
