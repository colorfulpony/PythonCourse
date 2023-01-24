import requests

url = "https://graph.facebook.com/v15.0/me?fields=id%2Cname&access_token=EAAIcJcs9N88BAFTYhUsZC6p5B3NvRspB8" \
      "0hU6NEfIrrt0c0f1Lyk0IEZAI8CY0LiaZB3EXtwh9bkiayaWK5E8ZBD5OsoGOLcF8trpv5faPNHuIEo8XMPZAIQzra0jZBw8kOdeZCZ" \
      "CWkZA4D78oSQuhPadXjsJRFVZA2ktUoKX7p1r3Www5xwNMwwBOADcw6QMTxnCEZABk8AabIAyjaCdM8q12SuZBMdRVnFas6se9ZCEOqz" \
      "jnJQ8GyoEN6tn5mRfnxxMzv8ZD"

response = requests.get(url)

print(response.content)
