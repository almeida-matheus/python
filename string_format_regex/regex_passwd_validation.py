import re

def validar_digito(senha):
    maiuscula = re.search(r'[A-Z]', senha)
    numero = re.search(r'[0-9]',senha)
    especial =  re.search(r'[!@#$%<^&*?]', senha)
    if len(senha) < 8 or len(senha) > 100:
        return 'digite pelo menos 8 caracteres'
    elif maiuscula == None:
        return 'digite pelo menos 1 caractere maiusculo'
    elif numero == None:
        return 'digite pelo menos 1 numero'
    elif especial == None:
        return 'digite pelo menos 1 caractere especial'
    else:
        print('senha OK')

senha = validar_digito('senhaDffff23??')
print(senha)
