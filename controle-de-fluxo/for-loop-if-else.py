'''
Enviar um email com os detalhes da compra online (maximo 3 tentativas) pra compras confirmadas
'''

compra_confirmada = True
dados_compra = 'compra no valor de R$ 12,30 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados no email')
        break
    else:
        print('Compra falhou')
