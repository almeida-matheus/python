import json

# dic -> object json
carros_dic = {
    "marca": "honda",
    "modelo": "hrv",
    "cor": "prata"
}

# list -> array json
carros_list = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]

# tuple -> array json
carros_tuple = ("honda", "volkswagem", "ford", "fiat", "chevrolet")

# CONVERTER PARA JSON
carros_json = json.dumps(carros_tuple)
print(carros_json)

carros_json = json.dumps(carros_dic, indent=2,
                         separators=(":", "="), sort_keys=True)
print(carros_json)

print("\n")

#GERAR ARQUIVO JSON
carros_dic = []

marca = 'honda'
modelo = 'hrv'
cor = 'prata'

carros_dic.append({
    'marca': marca,
    'modelo': modelo,
    'cor': cor
})

with open ('carros.json', 'w', encoding='utf8') as json_file:
    json.dump(carros_dic, json_file, indent=4, ensure_ascii=False, sort_keys=True, separators=(',',':'))
