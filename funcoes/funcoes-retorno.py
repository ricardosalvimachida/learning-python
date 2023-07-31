'''
Funcoes 
DRY - dont Repeat yourself
    Relaizam uma tarefa ou
    calcula um valor
'''


def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'


x = cliente1('Maria')
y = cliente2('jose')

print(x)
print(y)
