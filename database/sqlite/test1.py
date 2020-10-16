'''
https://pt.stackoverflow.com/questions/443332/express%C3%A3o-regular-para-validar-uma-senha-com-python
import re
from django.forms import forms

def test_password(password):
    minimal_number = 2
    minimal_upper_char = 2
    minimal_lower_char = 2
    minimal_special_char = 1
    minimal_len_char = 10
    if len(password or ()) < minimal_len_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_len_char)+' caracteres')
    if len(re.findall(r"[A-Z]", password)) < minimal_upper_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_upper_char)+' letras maiusculas')
    if len(re.findall(r"[a-z]", password)) < minimal_lower_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_lower_char)+' letras minusculas')
    if len(re.findall(r"[0-9]", password)) < minimal_number:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_number)+' numeros')
    if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", password)) < minimal_special_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_special_char)+' caracteres especiais')
'''
import re

def valida(senha):
    return (re.search(r'[0-9]', senha) and \
            re.search(r'[a-z]', senha) and \
            re.search(r'[A-Z]', senha) and \
            re.search(r'[!@#$%<^&*?]', senha) and \
            re.match(r'^[a-zA-Z0-9!@#$%<^&*?]{8,}$', senha)) \
           or re.match(r'^[a-zA-Z]+([- .,_][a-zA-Z]+){4,}$', senha)
print(valida('senha123E!05'))