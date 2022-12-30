"""
Manipulando chaves e valores em dicionários
"""
pessoa = {}

##
##

chave = "nome"

pessoa[chave] = "Gercyano"
pessoa["sobrenome"] = "Alves"

print(pessoa[chave])

pessoa[chave] = "Paula"

# del pessoa["sobrenome"]
print(pessoa)
print(pessoa["nome"])

if pessoa.get("sobrenome") is None:
    print("NÃO EXISTE")
else:
    print(pessoa["sobrenome"])


