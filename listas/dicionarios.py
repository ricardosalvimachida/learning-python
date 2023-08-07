# Lists
# armazenar mais informação em variáveis
# manter a sequencia de uma variável


# aluno = {} #Cuidado isso não é um set
aluno = {'nome': 'Ricardo', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

print(aluno)
print(aluno['nome'])

# atualizando dicionario
# aluno['nome'] = 'Greg'

aluno.update({'nome': 'ricardo Saklvi', 'nota_final': 'B'})
aluno.update({'endereco': 'osasco'})
msg = aluno.get('altura', 'Não existe')
print(aluno)
print(msg)

del aluno['idade']
print(aluno)
