import requests
from bs4 import BeautifulSoup

alamat_web = requests.get('https://oto.detik.com/', params={'tag_from': 'wp_firstnav_detikOto'})
soup = BeautifulSoup(alamat_web.text, 'html.parser')
# print (alamat_web.text)

news_feed = soup.find(attrs={'class': 'section nhl'})

# judul = soup.findAll(attrs={'class': 'ai_replace_title'})
# print(judul)

for i, judul in enumerate(news_feed.findAll('div', 'ai_replace_title'),1):
    judul = judul.text
    print(i, judul)

# for index, i in enumerate(news_feed.findAll('article', 'ph_newsfeed_d article_inview list-content__item'),1):
#         print(index, judul, i.get('i-img'), i.get('i-link'))




# print(judul.findAll('div').get_text())



# new = list(dict.fromkeys(a))
# print(new)
#
# for z in news_feed.findAll(attrs={'class': 'media__image'}):
#     print(z)
#
# for h in z.findAll('a', 'dtr-ttl'):
#     print(h)

#
# for judul in news_feed.findAll('a', 'ai_link media__link'):
#     print(judul.get('dtr-ttl'))
#     a = judul.get('dtr-ttl')
#     print(a)

# artikel = news_feed.findAll('article', 'ph_newsfeed_d article_inview list-content__item')
# print (artikel)



