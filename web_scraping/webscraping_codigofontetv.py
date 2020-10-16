# -*- encoding: utf-8 -*-
# esse script foi feito pelo canal codigo fonte tv, esta aqui por estudo
'''
requests2==2.16.0
pandas==1.0.1
lxml==4.5.0
beautifulsoup4==4.8.2
selenium==3.141.0
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1 - Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
top10ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
}

def buildrank(type):

    field = rankings[type]['field']
    label = rankings[type]['label']
    #simular click no elemento
    driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()
    #pegar elemento = tabela
    element = driver.find_element_by_xpath(
        "//div[@class='nba-stat-table']//table")
    #trazer o html do elemento
    html_content = element.get_attribute('outerHTML')

    # 2 - Parse HTML (Parsear o conteúdo HTML) - BeaultifulSoup
    #colocar como um dado estruturado, parsea ele
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # 3 - Data Structure Conversion (Estruturar conteúdo em um Data Frame com dados puros, elimina a parte do html) - Pandas
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']

    # 4 - Convert to Dict (Transformar os Dados em um Dicionário de dados próprio)
    return df.to_dict('records')


option = Options()
option.headless = True #True: tudo acontece em background
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(10)  # in seconds

for k in rankings:
    top10ranking[k] = buildrank(k)

driver.quit()

# 5 - Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
with open('ranking.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(top10ranking, indent=4)
    jp.write(js)
