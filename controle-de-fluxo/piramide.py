'''
Criar um Quadrado assim 6x6

     @
    @@
   @@@
  @@@@
 @@@@@
@@@@@@
'''

tamanho = 8

for tam in range(tamanho):
    quant = (tamanho - tam) - 1
    espace = ' ' * quant
    simbol = '#'*(tam+1)
    print(espace + simbol)
