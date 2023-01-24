import requests
def get_news(country, api_key='bcd076c6a81246efa69fc1a8a32e0b30'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n', {article['title']}, '\nDescription\n', {article['description']}")
    return results

content = get_news(country="ua")

print(content)
