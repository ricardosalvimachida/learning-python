# Criar promoção que cai de 5 em 5 todo dia até o valor de 20 reais


valor = 100
dia = 1
while valor > 20:
    print(f'No dia {dia} o produto vai ser vendido por {valor}')
    dia += 1
    valor -= 5
