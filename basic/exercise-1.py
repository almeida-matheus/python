'''
ler a quantidade de pessoas que serão convidadas para a festa
perguntar o nome de todas as pessoas e colocar em uma lista
imprimir todos os nomes da lista
'''

print('digite os nomes separados por um espaço\n')
guests = input('pessoas convidadas para a festa: \n')
separete_guests = guests.split(' ')
quantity = len(separete_guests)
print('quantidade de convidados:', quantity,)
print('convidados:',separete_guests,)
