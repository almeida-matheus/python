try:
    adds()
except NameError:
    print('vc digitou algo errado')

try:
    a = 12/0
except Exception as erro:
    print('aconteceu o erro:', erro)
else: #executa se nao tiver nenhum erro
    print('seu codigo passou sem erro')
finally: #sempre executada
    print('util pra fechar um arquivo por ex')

import time

def abre_arquivo():
    try:
        open('arquivo.txt')
        return True
    except Exception as erro1:
        print("aconteceu o erro:", erro1)
    return False

while not abre_arquivo():
    print('tentando abrir o arquivo')
    time.sleep(10)

print('consegui abrir o arquivo')
