# Unpacking Lists
# armazenar mais informação em variáveis
# manter a sequencia de uma variável

produtos = ['item1', 'item2', 'item3', 4, 5, 6, 7, 'item8']
item1, item2, item3, *outros = produtos


print(item1)
print(item2)
print(item3)
print(*outros)
