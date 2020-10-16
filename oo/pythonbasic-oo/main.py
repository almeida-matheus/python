from vehicle import Veiculo
from carro import Carro
caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print(caminhao_rosa)
print(type(caminhao_rosa))

print("cor:", caminhao_rosa.cor)
print("rodas:", caminhao_rosa.rodas)
print("marca:", caminhao_rosa.marca)
print("tanque:", caminhao_rosa.tanque)
caminhao_rosa.abastecer(100)
print("tanque:", caminhao_rosa.tanque, "\n")

carro_azul = Carro('azul', 'fiat', 5)
print("cor:", carro_azul.cor)
print("rodas:", carro_azul.rodas)
print("marca:", carro_azul.marca)
print("tanque:", carro_azul.tanque)
carro_azul.abastecer(46)
print("tanque:", carro_azul.tanque)