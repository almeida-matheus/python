import requests
from bs4 import BeautifulSoup
import re

url = 'https://almeida-matheus.github.io/front-end/viagem_r/index.html'

req = requests.get(url) #todo o html do site
req.encoding = 'utf-8'

soup = BeautifulSoup(req.text, 'html.parser') #para retornar os dados html parseados, mais legivel

links = []
for link in soup.find_all(attrs={'href': re.compile("http")}):
    links.append(link.get('href'))
for link in soup.find_all(attrs={'src': re.compile("http")}):
    links.append(link.get('src'))
    #print(link.get('src'))
print('\n'.join(links)) #junta as listas colocando um caractere
