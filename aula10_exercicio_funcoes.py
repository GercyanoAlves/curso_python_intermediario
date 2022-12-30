"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebudi como parâmentro
"""

# def duplicar(duplica):
#         return f"O dobro de 2 é {duplica*2}"

# def triplicar(triplica):
#         return f"O triplo de 2 é {triplica *3}"

# def quadruplicar(quadruplica):
#         return f"O quadruplo de 2 é {quadruplica *4}"

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def exercicio(multiplicador): # o multiplicador é um paramentro (valor para leigos)
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = exercicio(2)
triplicar = exercicio(3)
quadruplicar = exercicio(4)

try:
    print(f"dobro: {duplicar(int(input('Digite: ')))}") #(2) é o valor dado para o paramentro multiplicador.
    print(f"triplo: {triplicar(int(input('Digite: ')))}")
    print(f"quadruplo: {quadruplicar(int(input('Digite: ')))}")
except ValueError:
    print("Programa encerrado")


