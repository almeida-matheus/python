frase = 'curso em video python' #c-0 e-6 v-9 p-15

print(frase[9:14]) #fatiamento
print(frase[9:14:2]) #pula de 2 em 2
print(len(frase)) #quantidade de caracteres
print(frase.count('o',0,14)) #contagem + fatiamento
print(frase.find('deo')) #em que endereço começa deo
print(frase.find('android')) #quando nao existe retorna o valor -1
print('curso' in frase) #se existe curso em frase
print(frase.replace('python', 'android')) #substitui python por android

print(frase.upper()) #coloca a string em maiusculo
print(frase.lower()) #coloca a string em minusculo
print(frase.capitalize()) #so a primeira letra em maisculo, resto minusculo
print(frase.title()) #todo inico de palavra fica em maiusculo

frase_split = frase.split() #divide a string, palavras viram listas c-0 e-0 v-0 p-0
print(frase_split)
print(frase_split[0]) #string do endereço 0
print('-'.join(frase_split)) #junta as listas colocando um caractere

frase1 = '   aprendendo python   '
print(frase1.strip()) #remove os espaços inuteiss
print(frase1.rstrip()) #remove o espaços inuteis do script / lsplit

'''
string[:-1] #retira o ultimo caractere

string.rstrip('/') #retira o ultimo caractere se for /
'''


