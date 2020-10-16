'''
open('c:\\windows\\arquivo.txt') # 2 barras representam 1 barra
open('/root/arquivo.txt')

open('arquivo.txt','rb') # b para abrir algo sem ser texto
open('arquivo.txt','a') # apprend adiciona ao final do arquivo
open('arquivo.txt','r')
open('arquivo.txt','w')
'''

arquivo = open('arquivo.txt', 'w')

arquivo.write("eae pessoal tudo bem?\n")

arquivo = open('arquivo.txt', 'r')

print(arquivo.read())

arquivo.close() #muito importante fechar o arquivo
#ou usar o context managers
with open('arquivo.txt') as arquivo:
    (arquivo)
'''
for i in range(1, 1000):
    arquivo.write(str(i)+"\n")

arquivo = open('arquivo.txt', 'r')

print(arquivo.read())

#ler uma linha de cada vez
for linha in arquivo:
    print(linha)
'''