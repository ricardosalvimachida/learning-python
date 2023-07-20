''' 
Quero o resultado no output
 O Ricardo tem 35 anos e mora na cidade de São Paulo
Mas quero colocar tudo e variável
'''

nome = 'Ricardo'
idade = 35
cidade = 'Osasco'

# Esse print vai dar erro
# print('O '+nome+' tem '+idade+' anos e mora na cidade de '+cidade+'.')

nome2 = 'Ricardo'
idade2 = str(35)
#ou podemos ter idade2 = str(idade2)
cidade2 = 'Osasco'

# Esse print vai dar certo
print('O '+nome2+' tem '+idade2+' anos e mora na cidade de '+cidade2+'.')
