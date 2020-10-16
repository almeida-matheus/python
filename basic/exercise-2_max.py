#funcao para retornar o maior valor
def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:  # varrer
        if item > maior_item:
            maior_item = item
    return maior_item

#receber os valores e colocar na lista
print("digite numeros e irei retornar o maior deles\n digite x para finalizar")
lista = []
numeros = ()
while numeros != 'x':
    numeros = input()
    lista.append (numeros)
lista.remove('x')

print(maior(lista))
#print(max(lista))

