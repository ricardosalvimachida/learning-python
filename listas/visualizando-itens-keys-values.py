# Lists
# armazenar mais informação em variáveis
# manter a sequencia de uma variável


# aluno = {} #Cuidado isso não é um set
aluno = {
    'nome': 'Ricardo',
            'idade': 16,
            'nota_final': 'A',
            'aprovacao': True,
            'Materias': ['Fisica', 'matematica']
}

print(aluno)
print(aluno.get('Materias'))
print(aluno.items())

print(aluno.values())
print(aluno.keys())
