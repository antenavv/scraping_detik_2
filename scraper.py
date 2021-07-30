import requests
from bs4 import BeautifulSoup

alamat_web = requests.get('https://oto.detik.com/', params={'tag_from': 'wp_firstnav_detikOto'})
soup = BeautifulSoup(alamat_web.text, 'html.parser')
# print (alamat_web.text)

news_feed = soup.find(attrs={'class': 'list-content'})
artikel = news_feed.find(attrs={'class' : 'ph_newsfeed_d article_inview list-content__item'})

print(news_feed.text)
# for i, n in enumerate(news_feed):
#     print(i, n.text)
