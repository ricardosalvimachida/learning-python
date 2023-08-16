temperatura = int(input('Qual a temperatura da Carne?'))

if temperatura < 48:
    print('Cozinhe 1 min!')
elif temperatura == 48:
    print('Selada')
elif temperatura <= 54:
    print('Ao ponto p mal')
elif temperatura <= 60:
    print('Ao ponto')
elif temperatura <= 65:
    print('Ao ponto p bem')
elif temperatura <= 71:
    print('Bem passada')
elif temperatura > 71:
    print('Fodeo')
