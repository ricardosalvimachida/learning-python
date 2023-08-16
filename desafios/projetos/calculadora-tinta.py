rendimento_tinta = int(input('Qual o rendimento da lata?'))
altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da parede?'))

def calcular_rendimento_tinta(metragem, rendimento_tinta):
    rendimento_parede = metragem/rendimento_tinta
    print(f'Precisa comprar {rendimento_parede} latas')

def calcular_metragem_parede(altura, largura):
    return float(altura*largura)

metragem = calcular_metragem_parede(altura, largura)
calcular_rendimento_tinta(metragem, rendimento_tinta)
