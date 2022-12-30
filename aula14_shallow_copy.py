# Método úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa(shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

dicionario1 = {
    "chave1": 1,
    "chave2": 2,
    "lista1": [0, 1, 2],
}

# dicionario2 = copy.deepcopy(dicionario1)
dicionario2 = dicionario1.copy()

dicionario2["chave1"] = 1000
dicionario2["lista1"][1] = 9999


print(dicionario1)
print(dicionario2)
