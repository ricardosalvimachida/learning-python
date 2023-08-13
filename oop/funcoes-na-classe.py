# Classes
# Frutas
# Objects: Abacate,Banana

# classe
class Funcionario:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


# objeto
usuario1 = Funcionario('Ricardo', 'Salvi')
usuari2 = Funcionario('Greg', 'Bicov')

# print(usuario1.nome)
# print(usuario1.sobrenome)
# print(usuario1.nome_completo())
# print(usuari2.nome)
# print(usuari2.sobrenome)
# print(usuari2.nome_completo())

print(usuario1.nome_completo())
print(Funcionario.nome_completo(usuario1))
