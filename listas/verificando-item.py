# Listas
# armazenar mais informação em variáveis
# manter a sequencia de uma variável

cor_cliente = input('Digite uma cor')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

# if 'amarelo' in cores:
#     print('Sim')
# else:
#     print('Não')

if cor_cliente.lower in cores:
    print('Em estoque')
else:
    print('Não temos em estoque')
