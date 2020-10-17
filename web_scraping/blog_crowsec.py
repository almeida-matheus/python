import requests
from bs4 import BeautifulSoup
import json

url = 'https://blog.crowsec.com.br/'

req = requests.get(url) #todo o html do site
req.encoding = 'utf-8'

#soup = BeautifulSoup(req.text, 'html.parser')
soup = BeautifulSoup(req.content, 'html.parser') #para retornar os dados html parseados, mais legivel

# div class = post-feed > contem todos os posts
# article class = post-card > é cada post dentro da div class post-feed
posts = soup.find_all('article',class_="post-card")

#array de posts
all_post = []

for post in posts:
    title_preview = post.find(class_='post-card-content-link') #nessa classe tem o title e preview, é util utilizar ela quando na classe de todos os posts tem mais de uma tag h2 por exemplo
    title1 = title_preview.find('h2').text
    title2 = title_preview.h2.text
    title = (post.find('h2').text)
    preview = (post.find('p').text)
    author_time = post.find(class_='post-card-byline-content')
    author = author_time.find('a').text
    time = author_time.find('time').text #texto entre a tag >blabla<
    time1 = author_time.find('time')['datetime'] #tag time e atributo datetime="2020-09-17"
    img = post.find(class_='post-card-image')['src'] #class='' e atributo src=''

    all_post.append({
        'title': title, 
        'preview': preview, 
        'author': author, 
        'time': time1
        })
    #transformar em arquivo json
    #indent: json organizado, ensure_ascii: tirar os espaços do json \u00f3
    with open('posts.json','w', encoding='utf8') as json_file:
        json.dump(all_post, json_file, indent=4, ensure_ascii=False)

'''
#se tiver paginacao
links = soup.find(class_="pagination").find_all('a') #econtrar todos os a dessa classe

all_req = []
for link in links:
    print(link.get('href')) #pegar todos os a e mostrar so o href
    req = requests.get(link.get('href'))
    all_req.append(BeautifulSoup(req.text, 'html.parser'))

for posts in all_req:
    posts = soup.find_all('article',class_="post-card") #excluir o de cima
    for post in posts:
        title_preview = post.find(class_='post-card-content-link')
        title1 = title_preview.find('h2').text
'''