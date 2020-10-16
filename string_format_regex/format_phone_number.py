#checa se o valor digitado é um numero
def check_number():
    while True:
        n=input('digite o numero com ddd: ')
        if n.isnumeric():
            break
        else:
            print('digite apenas numeros \n')
    return n
#formata o valor digitado para (xx)x-xxxx-xxxx
def format_number(n):
    try:
        n=n.lstrip('0') #retirar o 0 do ddd
        #n=int(n) #se tiver letras resultara em ValueError
        if len(n) != 11:
            raise ValueError
        else:
            n=str(n)
            n_formatted='({}){}-{}-{}'.format(n[0:2],n[2] ,n[3:7],n[7:])
            print(n_formatted)
    except ValueError:
        print('numero invalido, precisa ter 11 numeros')

n=check_number()
format_number(n)
#!/usr/bin/env python3