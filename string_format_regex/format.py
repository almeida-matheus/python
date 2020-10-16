str = 'O filme {0} merece {1} estrelas'
str.format('Exterminador do Futuro', 4)
print(str)
print('\n')

texto = '{0} tem {idade} anos de idade'
print('Progama para calcular a idade de uma pessoa')
print()

nome = input('Entre com o nome da pessoa: ')
print()

a1 = int(input("Entre com o ano de nascimento: "))
print()

a2 = int(input("Entre com ano atual: "))
print()
print(texto.format(nome, idade = a2 - a1 ))

s = 'Adoro Python'
print('\n')

# alinha a direita com 20 espaços em branco
print("{0:>20}".format(s))

# alinha a direita com 20 símbolos #
print("{0:#>20}".format(s))

# alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
print("{0:^20}".format(s))

# imprime só as primeiras cinco letras
print("{0:.5}".format(s))
print('\n')

# Programa para calcular a media de um aluno
print('Programa para calcular a media de um aluno')
print()

nome = input('Entre com o nome do aluno: ')
print()

nota1 = float(input("Entre com a primeira nota: "))
print()

nota2 = float(input("Entre com a segunda nota: "))
print()

media = (nota1 + nota2)/2
print('{0} teve media igual a: {1:4.2f}'.format(nome, media))

fruta='laranja'
print('suco de %s é bom' %fruta)

cor1='azul'
cor2='rosa'
print('o céu é {0} a flor é {1} e o carro é {0}'.format(cor1, cor2))

conta=17/3 #2 casas decimais apos virgula
print('resultado da conta é:{:.2f}'.format(conta))

calculo=17/3
calculo='%.2f' % calculo
print(calculo)

def phone_number():
    x='123456789'
    print('{}-{}-{}'.format(x[:3],x[3:6],x[6:]))

