"""
Exercícios com funções

Crie uma função que mutiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variával e mostre o valor 
da variável.
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        print(f"Mutiplicação: {total} * {numero}")
        total *= numero
        print(f"Resutado: {total}")
    return total
    

valor = multiplicar(5,7,8)
print(f"O Resultado mutiplicado da função é: {valor}")

# Crie uma função que fala se um número é par ou impar.
# Retorne se o número é par ou impar.

def par_impar(numero):
    divisivel = numero % 2 == 0

    if divisivel:
        return f"{numero} é par"
    return f"{numero} é impar"

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
