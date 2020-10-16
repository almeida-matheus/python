'''
this is my first program in python
basic, variables, if and else, strings and lists
'''

name = 'matheus almeida costa'
age = 19
print( 'my name is', name, 'and I am', age, 'years old',)
#converter tipo int para str
print('my name is ' + str(name))

age_user = input('\n how old are you?\t')
age_user = int(age_user)
print(age_user)
print(type(age_user))

#comando if not faz o contrario da condição do if
if age_user == 18:
    print('you are 18, so you are a new major\n')
elif age_user >= 18:
    print('you are a major\n')
else:
    print('you are minor\n')

name_list = ['seiya', 'shiryu', 'hyoga', 'shun', 'ikki',]
name_list.append('jabu') #inserir no ultimo caractere
name_list.remove('ikki')
name_list.insert(0,'saori')
name_list[0] = 'atena'
counter = name_list.count('shiryu') #quantos vezes shiryu aparece
print(name_list.pop()) #printa o ultimo e tira ele
print (type(name_list))
print(name_list)
print(name_list[::-1]) #valores de trás para frente
print(name_list[0:5:2]) #de 0 a 5 (don't show the 5) pulando a cada 2 caracteres // o ultimo valor da lista é -1
separe_name = name.split(' ')#converter string para lista
print(separe_name)