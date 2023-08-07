from array import array
# Lists  - Array
# armazenar mais informação em variáveis
# manter a sequencia de uma variável

letras = ['a', 'b', 'c', 'd']
numero_i = [10, 20, 30, 40]
numero_f = [1.1, 2.2, 3.3, 4.4]

print(letras)
print(numero_i)
print(numero_f)

letras = array('u', ['a', 'b', 'c', 'd'])
numero_i = array('i', numero_i)
numero_f = array('f', numero_f)

print(letras)
print(numero_i)
print(numero_f)
