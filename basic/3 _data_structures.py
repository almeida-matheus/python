'''
estrutura de dados
'''

lista = ['shiryu', 'seiya'] #dinâmica / para saber ordem
lista1 = []
tupla = ['shiryu', 'seiya'] #tamanho fixo / numero definido de coisas
tupla1 = ()
dicionario = {'nome': 'matheus', 'idade': 19} # dict = chave e um valor dinamico
dicionario1 = {}
conjunto = {'shiryu', 'seiya'} #somente o valor, nao existe repetidos, nao existe indice de ordenacao, dinamico
conjunto1 = set()

dicionario['nome'] = 'matt'
dicionario['local'] = 'casa'

if 'shiryu' in conjunto: #nao funciona em dicionario // util em conjunto pq eh uma tabela hash diferente da lista q tem q comparar
    print('shiryu esta na lista')
if 'matheus' in dicionario.values():
    print('matheus esta no dicionario')

for valores in dicionario.keys():
    print(valores)

print (dicionario['nome'])

conjunto.add('hyoga')
print (len(conjunto))

loucura = [ (1,2), (3,4), ({'joao', 'maria'}, {'gabriel'})]
print(loucura)