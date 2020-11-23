import re
#search - procura, se nao tiver = None
#findall - retorna uma lista
#sub - substituir
#compile
string='este é apenas um teste do teste'
print(re.search(r'teste', string))
print(re.findall(r't...e', string))
print(re.sub(r'teste','ABC', string, count=1))
print(re.findall(r'[a-zA-Z0-9]este', string))
print(re.findall(r'TeStE', string, flags=re.IGNORECASE))
#or
print('\n')
regexp=re.compile(r'[Tt]este|este')
print(regexp.findall(string))
print(regexp.sub('ABC', string))

a = 'Maria  Eduarda'
regex = re.compile(fr'Maria\s+Eduarda', flags=re.IGNORECASE) #\s - 1 ou mais espaços
print(regex.search(a))

#meta caracteres:
# * - 0 ou n vezes 
# + - 1 ou n vezes
# ? - 0 ou 1

# ^ - começa com
# $ - termina com
# [^a-z] - qualquer coisa q nao seja de a ate z