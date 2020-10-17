import json

#CONSURMIR ARQUIVO JSON EXTERNO

path = 'D:\\Arquivos\\matheus\\Documents\\Code\\python\\string_format_regex\\jogador.json'

#LOAD: arquivo externo, LOADS: string do script
with open(path, 'r') as json_file:
    jogador_dic = json.load(json_file)

#itens
for i in jogador_dic[1].items():
    print(i)

print(jogador_dic[1]["nome"])
