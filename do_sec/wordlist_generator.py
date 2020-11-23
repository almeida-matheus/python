import string
from itertools import combinations_with_replacement
import time

def main(valores, tamanho):
    #calculo do tempo
    init_t = time.time()
    gerar_senhas(valores, tamanho)
    fin_t = time.time()

    tempo = (fin_t - init_t)
    tempo_2_decimais = '%.2f' % tempo
    print("time:",tempo_2_decimais + "s")

def gerar_senhas(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho) #('a', 'a', 'a', 'a')
    lista = list(comb)
    print("combinations:", str(len(lista)))

    #gerar wordlist
    with open('wordlist.txt','w') as arquivo: 
        for valor in lista: #antes: ('a', 'a')
            valor = ''.join(valor) #depois : aa
            arquivo.write(str(valor) + '\n')

def menu():
    print('---------------------------------------')
    print('WORDLIST COMBINATION')
    print('1 - just lowercase')
    print('2 - just numbers')
    print('3 - lowercase and uppercase')
    print('4 - lowercase and numbers')
    print('5 - lowercase, uppercase and numbers')
    print('---------------------------------------')

if __name__ == '__main__':
    menu()

    op = input('selected option: ')
    
    if op not in ['1', '2', '3', '4', '5']:
        print('error: invalid option')
        exit

    if op == '1':
        valores = string.ascii_lowercase

    if op == '2':
        valores = string.digits
    
    if op == '3':
        valores = string.ascii_letters

    if op == '4':
        valores = string.ascii_lowercase
        valores += string.digits
    
    if op == '4':
        valores = string.ascii_letters
        valores += string.digits

    try:
        tamanho = int(input('enter the size of the combination: '))
        main(valores, tamanho)
    except ValueError as erro:
        print('it is not an integer')
    except Exception as erro:
        print('error:', type(erro))
        

    