#apt-get install python3-pip
#pip3 install requests
#python3 -m pip install requests
#pegar a pagina/titulos: Beautiful soup 4 // pip install bs4
import requests
texto = None
try:
    requisicao = requests.get('https://solyd.com.br')
    #print(requisicao.text) #codigo fonte do site
except Exception as erro:
    print('erro:', erro)

#site: putsreq.com
#Referer: de q site a pessoa veio
cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https://google.com.br'}
meus_cookies = {'Ultima-visita': '10-10-2020'}
dados = {'username': 'guigui', 'password': 'gui123'}
req = requests.post('https://putsreq.com/hC6YMT5EAazWFfLiJORi',
                    headers=cabecalho,
                    cookies=meus_cookies,
                    data=dados)
#print(req.text)

#request
#get = receber informacao do servidor
#post = enviar informacoes ao servidor
#response
#html, json(dados), cod status

payload = {"firstName": "matheus", "lastname": "Smith"}
r = requests.post("https://httpbin.org/post", data=payload)
#print(r.text)
