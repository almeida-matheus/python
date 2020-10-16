'''
SOFTWARE DE GERENCIAMENTO BANCARIO
-criar clientes e contas
-cada cliente possui: nome, cpf, idade
-cada conta possui: cliente, saldo, limite, sacar, depositar, consultar
'''

from cliente import Cliente
from conta import Conta

cliente1 = Cliente('roberto', '402', 35)

conta_roberto = Conta(cliente1, 20, 400)

#print(cliente1)

#print(conta_roberto.cliente)

conta_roberto.sacar(430)
print(conta_roberto.saldo)