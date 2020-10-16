'''
this is my second program in python
for and while
'''

name_list = ['seiya', 'shiryu', 'hyoga', 'shun', 'ikki',]

for x in name_list:
    print(x)
print('\n')
for i in range(len(name_list)): #len retorna a quantidade de caracteres
    print(name_list[i])
print('\n')
for letter in name_list[1]:
    print(letter)
print('\n')

z = 0
x = 0
while z < 4:
    print(z, 'is less than 4')
    z = z + 1
print('now is', z,)
print('\n')
# i += 1 is same thing than i = i + 1

while True :
    print(x)
    if x == 3:
        break
    x += 1

