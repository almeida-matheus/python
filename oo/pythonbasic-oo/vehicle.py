
class Veiculo:
    #criar metodo self: o objeto passa ele msm la dentro
    #metodo eh o construtor
    #self.cor = cor  pq quando iniciar o objeto cor jogar na varial self.cor
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros
