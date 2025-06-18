from bs4 import BeautifulSoup
import requests

# with open('simple.html','r') as html_file:
#     soup = BeautifulSoup(html_file,'lxml')

# print(soup) #print without any indent
# print(soup.prettify()) #print with proper indents

#Accessing individual tags of html

# match = soup.title #Accesses whole title and only the first title tag
# match = soup.title.text #accesses only the text and only the first title tag
# print(match)

# match = soup.find('div',class_='content2') #if we do not specify class or id it also gives the first div it find
# match = soup.find('div',id='content2')
# print(match)
# paragraph = match.find_all('p') #find all the elements with p tag
# print(paragraph)

# for article in soup.find_all('div',class_='article'):
#     headline = article.find_all('p')
#     for p in headline:
#         print(p.text)

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

article = soup.find('article')
# print(article)

vid_src = article.find('iframe',class_='youtube-player')['src']#to get specific attribute we can treat it like dict
# print(vid_src)
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
