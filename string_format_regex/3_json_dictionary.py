import json
'''
jogador_json = {
    "nome": "matheus",
    "time": "cruzeiro",
    "escalado": "True",
    "energia": 100,
    "mochila": ["corda", "flecha"],
    "aeronave": [
        {"tipo": "transporte", "habilidade": 80},
        {"tipo": "ataque", "habilidade": 100},
        {"tipo": "reconhecimento", "habilidade": 50}
    ]
}
'''
jogador_json = '{"nome": "matheus", "time": "cruzeiro", "escalado": "True", "energia": 100, "mochila": ["corda", "flecha"], "aeronave": [{"tipo": "transporte", "habilidade": 80}, {"tipo": "ataque", "habilidade": 100}, {"tipo": "reconhecimento", "habilidade": 50}]}'

jogador_dic = json.loads(jogador_json)

'''
#todas chaves
for c in jogador_dic:
    print(c)

#todas valores
for v in jogador_dic:
    print(v)
'''
#itens
for i in jogador_dic.items():
    print(i)

#print(jogador_dic["nome"])

for i in jogador_dic["mochila"]:
    print(i)

for a in jogador_dic["aeronave"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))