
class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite


    def sacar(self, qnt):
        if self.saldo - qnt < self.limite:
            print("saldo insuficiente")
        else:
            self.saldo -= qnt
            print("foi sacado:", qnt)

    def depositar(self, qnt):
        if qnt > 0:
            self.saldo += qnt
            print("foi depositado:", qnt)
        else:
            print("erro no deposito")

    def consultar(self):
        return self.saldo
