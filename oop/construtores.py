# Classes
# Frutas
# Objects: Abacate,Banana

# classe
class Funcionario:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# objeto
usuario1 = Funcionario('Ricardo', 'Salvi')
usuari2 = Funcionario('Greg', 'Bicov')

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuari2.nome)
print(usuari2.sobrenome)
