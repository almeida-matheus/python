#herdar caracteristicas da classe pai: Veiculo

from vehicle import Veiculo
#td vez q ele ta iniciando o carro ele esta criando um veiculo
class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    #sobreposicao
    #novo metodo abastecer exclusivo pra Carros/ caminhao continua ilimitado
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("erro: tanque cheio")
        else:
            self.tanque += litros
