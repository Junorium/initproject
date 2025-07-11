
import requests
from bs4 import BeautifulSoup

def scrape_news(keyprompt):
    url = f"https://news.google.com/search?q={keyprompt}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    articles = []

    for a in soup.select('article h2'):
        text = a.get_text(strip=True)
        if text:
            articles.append({'title': text})
    return articles[:5]