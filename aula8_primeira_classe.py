"""
Higher Order Functions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): # <- Empacota paramentros
    return funcao(*args) # <- Desempacota paramentros

# v = executa(saudacao)

print(executa(saudacao, "Bom dia", "Gercyano"))
print(executa(saudacao, "Bom noite", "Paula"))