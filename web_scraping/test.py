# 
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/playlist?list=PLMKi-ss_sEoNy9Fi4FYDR6Nu6PD-WkpCL'
# url = 'https://www.youtube.com/watch?v=inocgEraxo0&list=PLMKi-ss_sEoNy9Fi4FYDR6Nu6PD-WkpCL&ab_channel=LilPeep'
req = requests.get(url) #todo o html do site

soup = BeautifulSoup(req.content, 'html.parser') #para retornar os dados html parseados, mais legivel

print(soup)

# soup = BeautifulSoup.BeautifulSoup('<html><body><div id="articlebody"> ... </div></body></html')
# soup.find("div", {"id": "articlebody"})


# div class = style-scope ytd-playlist-video-list-rendere > contem todos os titulos
# ytd-playlist-video-renderer class = style-scope ytd-playlist-video-list-renderer > é cada titulo dentro da div
list_titles = soup.find_all('span',class_="style-scope ytd-playlist-panel-video-renderer")
res = soup.find_all('span',{'class':'style-scope ytd-playlist-panel-video-renderer'})

print (soup.find(id='video-title'))

print(res)

##outro teste
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=inocgEraxo0&list=PLMKi-ss_sEoNy9Fi4FYDR6Nu6PD-WkpCL&ab_channel=LilPeep'

data = requests.get(url)
# soup = BeautifulSoup(data.content, 'html.parser')
soup = BeautifulSoup(data.content, 'lxml')
# print(soup)

h4 = soup.find_all("h4")
res = soup.find_all('h4')
posts = soup.find_all('div',class_="playlist-items yt-scrollbar-dark style-scope ytd-playlist-panel-renderer")

print(res)
for title in soup.find_all('span', id="eow-title"):
    print(title.get_text('\n'))

for h in h4:
    print(h.text)