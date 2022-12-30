"""
Closore e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Bom noite")

for nome in ["Gercyano", "Ana Paula", "Valentina"]:
    print(bom_dia(nome))
    print(boa_noite(nome))