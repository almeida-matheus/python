#pip install selenium
#pip install webdriver_manager
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#campo de pesquisa: class="_3FRCZ copyable-text selectable-text"

#navegar ate o wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
#definir grupos/contatos e mensagem
contatos=['Davidson', 'Ilza']
mensagem = 'mensagem teste'
#buscar contatos/grupos e realizar as funcoes
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]'
        )
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
#campo de pesquisa de pesquisar contato e de enviar mensagem é igual
#o segundo deve ser elementS, campo de cima é indexado como 0 o de baixo é 1
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]'
        )
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
