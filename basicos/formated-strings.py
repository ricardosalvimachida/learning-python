# Formatar o print para fazer igual o texto abaixo
# O Ricardo Salvi e um excelente [Programador]

nome = 'Ricardo'
sobrenome = 'Salvi'
profissao = 'Programador'

# sem formater
texto = 'O '+nome+' '+sobrenome+' e um excelente ['+profissao+']'
# com formater fica mais legível
texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'

print(texto)
print(texto2)
