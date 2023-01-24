import requests

# r = requests.get("https://newsapi.org/v2/everything?q=united%20state&from=2022-12-24&sortBy=publishedAt&apiKey=bcd076c6a81246efa69fc1a8a32e0b30")
# content = r.json()

def get_news(topic, from_date, api_key='bcd076c6a81246efa69fc1a8a32e0b30'):
    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=publishedAt&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n', {article['title']}, '\nDescription\n', {article['description']}")
    return results

content = get_news("tesla", 2022-12-24)

print(content)
