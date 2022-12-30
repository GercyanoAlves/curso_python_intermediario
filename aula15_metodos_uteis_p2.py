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

p1 = {
    "nome": "Gercyano",
    "sobrenome": "Alves",
}

# print(p1["nome"])
# print(p1.get("nome"))

# nome = p1.pop("nome")
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave, " <- Dicionário deletado.")
# print(p1, "<- Dicionario atualizado.")

# p1.update({
#     "nome": "Novo Valor",
#     "idade": 31,
# })

# p1.update(nome="novo valor", idade=31)
# tupla = (("nome", "novo valor"), ("idade", 31))
lista = [["nome", "novo valor"], ["idade", 31]]
p1.update(lista)
print(p1)