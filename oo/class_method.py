class Computador:
    def __init__(self, marca, ram, armazenamento): #propriedades
        self.marca = marca
        self.ram = ram
        self.armazenamento = armazenamento
    
    def Ligar(self): #metodos
        print('estou ligando')
    
    def Desligar(self): #metodos
        print('estou desligando')
    
    def Exibir_Info(self): #metodos
        print(self.marca, self.ram, self.armazenamento)

computador1 = Computador('asus', 8, 120)
computador1.Exibir_Info()
