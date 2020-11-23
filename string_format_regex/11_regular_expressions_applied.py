import re
import requests
#site: regex101

requisicao = requests.get('http://www.coltec.ufmg.br/coltec-ufmg/?page_id=34')
string_teste = 'o gato é bonito'

padrao = re.search(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao: #se existir alguma coisa em padrao
    print(padrao.group())
else:
    print('padrao nao encontrado')
