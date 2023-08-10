try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Digite um valor de numero')
finally:
    print('Codigo ok')


# else:
#     print('Digitou errado!')
#     resultado = valor*2
#     print(resultado)

print('Continua')
