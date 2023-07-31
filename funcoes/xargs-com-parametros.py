def agencia(**carro):
    return carro


x = agencia(marca='Gol', cor='Branco', motor='1.0')
y = agencia(marca='Gol', cor='Branco')
z = agencia(marca='Gol', cor='Branco', motor='1.0', placa='XPTO')

print(x)
print(y)
print(z)
