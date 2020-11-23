
#f antes das aspas para formatar
# f'{self.marca}' = asus / '{self.marca}' = {self.marca}

class Computador:
    def __init__(self, marca, ram, armazenamento):
        self.marca = marca
        self.ram = ram
        self.armazenamento = armazenamento

    def Estado(self, energia):
        self.energia = energia
        if energia == 0:
            print(f'o pc da {self.marca} esta desligando')
            self.energia = False
        elif energia == 1:
            print(f' o pc da {self.marca} esta ligando')
            self.energia = True
        else:
            print('comando não reconhecido')

    def ExibirInfo(self):
        print('marca:',self.marca, 'ram:',self.ram, 'armazenamento:',self.armazenamento)
        if self.energia:
            print('está ligado')
        if not self.energia:
            print('está desligado')

computador1 = Computador('asus', 8, 120)
computador1.Estado(0)
computador1.ExibirInfo()

