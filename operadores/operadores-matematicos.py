'''
Ordem de prevalencia( quem vem primeiro)
Parenteses -> Exponenciais -> Multiplicação/Divisão -> Soma e Subtração 

'''

calculo = 2 + 2
print(calculo)

# multiplicação tem prevalencia
calculo2 = 2 + 2 * 3
print(calculo2)

calculo3 = 2 + 2 * 3 / 2
print(calculo3)

# parenteses força a prevalencia
calculo4 = (2 + 2) * 3 / 2
print(calculo4)

# exponencial tem prevalencia apos o parenteses
calculo5 = 4 / 2 + 2 ** 3
print(calculo5)
