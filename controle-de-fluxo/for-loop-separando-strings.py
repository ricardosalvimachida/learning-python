# Separar palavra com espaços
# Exemplo OSASCO => O S A S C O


palavra = 'OSASCO'

# jeito 1
for letra in palavra:
    print(f' {letra}', end='')

print('\n===========')
# jeito 2
for letra in palavra:
    print(letra, end=' ')
