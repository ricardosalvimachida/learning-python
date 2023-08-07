# Lists
# armazenar mais informação em variáveis
# manter a sequencia de uma variável


# aluno = {} #Cuidado isso não é um set
aluno = {'nome': 'Ricardo', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

for x in aluno:  # .keys()
    print(x)

for x in aluno.values():
    print(x)

for x in aluno.items():
    print(x)

for keys, values in aluno.items():
    print(keys, values)
