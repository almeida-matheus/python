import requests
from bs4 import BeautifulSoup

url = 'https://ufmg.br/comunicacao/noticias/todas-as-noticias?pagina=1'

req = requests.get(url) #todo o html do site

soup = BeautifulSoup(req.content, 'html.parser') #para retornar os dados html parseados, mais legivel

lista_noticias = soup.find_all('ol',class_="link-list") #buscar todas as tags que tem ol (onde agrupa todas as noticias)

for lista_titulos in lista_noticias:
    lista = lista_titulos.find_all('h1',class_="link-list__title") #dentro da lista_noticias filtrar pela tag e classe de titulo
    for lista_dados in lista:
        print(lista_dados.next_element) #nao pegar a tag html, e sim oq ta apos o elemento <>pega esse<>


