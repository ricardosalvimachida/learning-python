# Functions
# DRY - Dont Repeat Yourself
# Quero usar uma função para somar qualquer número
# numero1 = 10
# numero2 = 2
# resultado = numero1 + numero2
# print(resultado)


# Vai dar erro

# def somar_dois_numeros():
#     numero1 = 10
#     numero2 = 2
#     resultado = numero1 + numero2
#     print(resultado)


# somar_dois_numeros()

# print(resultado)
# Vai dar erro pq resultado não é global


# Esse abaixo vai dar certo
def somar_dois_numeros():
    numero1 = 10
    numero2 = 2
    resultado = numero1 + numero2
    print(resultado)


def somar_dois_numeros2():
    numero1 = 10
    numero2 = 7
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()
somar_dois_numeros2()
