renda_acima_5k = True
nome_limpo = True


# preciso dos dois True para passar
if nome_limpo and renda_acima_5k:
    print('Financiamento APROVADO')
else:
    print('Financiamento Negado')

# preciso de pelo menos um True para passar
if nome_limpo or renda_acima_5k:
    print('Financiamento APROVADO')
else:
    print('Financiamento Negado')
