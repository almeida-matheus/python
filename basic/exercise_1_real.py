'''
ler a quantidade de pessoas que serão convidadas para a festa
perguntar o nome de todas as pessoas e colocar em uma lista
imprimir todos os nomes da lista
'''

x = 1
lista = []
quantity = input('quantidade de pessoas convidadas: ')
quantity = int(quantity)
while x < quantity + 1:
    guests = input('nome do convidado'+ str(x) +': ')
    lista.append(guests)
    x = x + 1
print ('lista de convidados:')
print('\n')
for a in lista:
    print(a)
print('\n')
z = 0
while z < quantity:
    print (lista[z])
    z = z + 1