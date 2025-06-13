import requests

r = requests.get('https://news.google.com/news/rss')

print(r.content)