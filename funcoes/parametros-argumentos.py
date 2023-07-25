# Functions
# DRY - Dont Repeat Yourself
# Fazer 3 olás, mas chamar uma funcao com parametros diferentes


def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops')


boas_vindas('Ricardo', 6)
boas_vindas('Greg', 12)
