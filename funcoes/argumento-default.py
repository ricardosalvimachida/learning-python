# Functions
# DRY - Dont Repeat Yourself
# Fazer 3 olás, mas chamar uma funcao com parametros diferentes
#Default = Aquele que vc define
#Não Default = Aquele que vc não define

def boas_vindas(nome, quantidade = 6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops')


#tenta rodar esse sem a quatidade default
# boas_vindas('Ricardo')
boas_vindas('Greg', 12)