# classe
from datetime import datetime


class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade = int(ano_atual - self.ano_nascimento)
        return idade


# objeto
usuario1 = Funcionario('Ricardo', 'Salvi', 1988)
usuari2 = Funcionario('Greg', 'Bicov', 2021)

# print(usuario1.nome)
# print(usuario1.sobrenome)
# print(usuario1.nome_completo())
# print(usuari2.nome)
# print(usuari2.sobrenome)
# print(usuari2.nome_completo())

print(usuario1.nome_completo())
print(Funcionario.nome_completo(usuario1))
print(Funcionario.idade_funcionario(usuario1))
