from bs4 import BeautifulSoup
import requests

def main():
    in_currency = input("Enter in currency symbol like USD:")
    out_currency = input("Enter out currency symbol like USD:")
    amount = input(f"Enter amount of {in_currency}:")

    current_rate = get_currency(in_currency, out_currency, amount)
    print(current_rate)

def get_currency(in_currency, out_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate

main()