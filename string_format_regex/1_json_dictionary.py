import json

#CONVERTER JSON PARA DICTIONARY
carros_json = '{"marca": "honda", "cor": "prata"}' #json

carros_dic = json.loads(carros_json) #converter json para o tipo do python: dictionary

print(carros_dic["marca"])

for x in carros_dic.values():
    print(x)

for k,v in carros_dic.items():
    print(k + " - " +v)

print("\n")

#CONVERTER DICTIONARY PARA JSON
carros_dic = {"marca": "honda", "cor": "prata"}

carros_json = json.dumps(carros_dic)

print(carros_json)
print(carros_dic)