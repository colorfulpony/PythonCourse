import requests
from fake_useragent import UserAgent
from datetime import datetime
import time

ticket = input("Enter the ticket symbol like 'TSLA':")
from_date = input("Enter start date in yyyy/mm/dd format:")
to_date = input("Enter end date in yyyy/mm/dd format:")

from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticket}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
ua_str = UserAgent().chrome

content = requests.get(url, headers={"User-Agent": ua_str}).content
print(content)

with open('data.csv', 'wb') as file:
    file.write(content)