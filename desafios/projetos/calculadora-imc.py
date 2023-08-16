altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso?'))

imc = peso/(altura/100)**2


if imc < 18:
    print('Magreza')
elif imc < 30:
    print('OK')
else:
    print('Obesis')
