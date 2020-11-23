import random

print(random.random()) #valor de 0.0 até 1.0
print(random.uniform(1,10)) #valor decimal do minimo ao maximo
print(random.randint(1,10)) #valor inteiro do minimo ao maximo

cores = ['azul', 'branco', 'verde']
print(random.choice(cores)) #escolher uma opção aleatoria

cartas = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas) #dar umam combinação diferentew
print(cartas)

print('____________________________')
#gerarador senhas simples

letras = 'abcdefghijklmnopqrstuvwxyz'
letras = list(letras)
tamanho_senha = 5
senha = ""

for i in range(tamanho_senha):
    senha += random.choice(letras)

print(senha)
print('____________________________')