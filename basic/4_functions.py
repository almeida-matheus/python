def soma(n1, n2):
    resp=n1+n2
    return resp
retorno = soma(25, 35)
print (retorno)

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
if tem_sete_itens("abcdefg"):
    print ("tem 7 itens")