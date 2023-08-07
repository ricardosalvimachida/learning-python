
# imprmir numeros multiplos de 10
from sys import getsizeof
numeros = [x*10 for x in range(5)]
print(numeros)

# imprimir com strings
frutas = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for item in frutas:
#     if 'b' in item:
#         frutas2.append(item)
# frutas = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = [item for item in frutas if 'x' in item]

print(frutas2)

##################################################################
# generator expressions

print('==============')
numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(getsizeof(numeros))
print('==============')

numeros = (x * 10 for x in range(1000))
print(type(numeros))
print(getsizeof(numeros))
