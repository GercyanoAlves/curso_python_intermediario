# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Gercyano', 'sobrenome': 'Alves'},
#     {'nome': 'Paula', 'sobrenome': 'Alves'},
#     {'nome': 'Valentina', 'sobrenome': 'Alves'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Gercyano', 'sobrenome': 'Alves'},
    {'nome': 'Paula', 'sobrenome': 'Alves'},
    {'nome': 'Valentina', 'sobrenome': 'Alves'},
]

l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])


def exibir(lista):
    for item in lista:
        print(item)
    print()


exibir(l1)
exibir(l2)