from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.dawn.com/').text
soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

# article = soup.find('article')

# title = article.h2.text
# link = article.h2.a['href']
# print(link)
# print(link)

for article in soup.find_all('article'):
    try:
        title = article.h2.text
        print('Title:',title)
        link = article.h2.a['href']
        print('Link:',link)
        print()
    except:
        title = None
        link = None
        print('Title:',title)
        print('Link:',link)
        print()