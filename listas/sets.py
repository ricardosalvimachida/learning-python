# Lists  - Sets
# armazenar mais informação em variáveis
# manter a sequencia de uma variável


# list1 = [10, 20, 30, 40]
# list2 = [10, 20, 50, 60, 70]

# num1 = set(list1)
# num2 = set(list2)
# # set perdem a ordem
# print(num1)
# print(num2)

# print(num1 | num2)  # Union
# print(num1 - num2)  # Difference
# print(num1 ^ num2)  # Simetric Difference
# print(num1 & num2)  # And

# print(len(num1))


#################################
#################################
#################################
#################################
# integer

# funcoes com sets
# print()
# list1 = set([1, 2, 3, 5, 6])
# s1 = {1, 2, 3, 5, 6}

# chaves vira set exceto dicionario {} assim vazio
# print(type(list1))
# print(list1)
# print(type(s1))
# print(s1)

# s1.add(7)
# print(s1)
# s1.update([7, 8])
# print(s1)
# s1.remove(7)  # gera erro se não tem
# print(s1)
# s1.discard(7) # nào gera erro se não tem
# print(s1)

# valores duplicados, mas mostra igual
# s1 = {1, 2, 3, 5, 6, 1, 2}
# print(s1)

#################################
#################################
#################################
#################################
# string

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
#diference
print(set4)

