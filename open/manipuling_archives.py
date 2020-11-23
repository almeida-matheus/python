'''
r > ler
w > escrever
r+ > ler e escrever
a > acrescentar
'''

valores_lista = ['a','b',43,543]

#digitar e sobrescrever a alista
with open('valores_lista.txt','w') as arquivo:
    for valor in valores_lista:
        arquivo.write(str(valor) + '\n')

#ler a lista
with open('valores_lista.txt','r') as arquivo:
    for valor in valores_lista: #esta lendo a vairavel e nao o arquivo txt
        print(valor)
print("________")
#ler e acrescentar
with open('valores_lista.txt','r+') as arquivo:
    for valor in arquivo: #esta lendo o arquivo txt
        print(valor)
    arquivo.write('99' + '\n')