

'''
Lista1: Funcionarios que tem carro e que trabalham a noite
Lista2: Funcionarios que tem carro e que trabalham de dia
Lista3: Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


func_carro_dia = set(tem_carro).intersection(turno_dia)
func_carro_noite = set(tem_carro).intersection(turno_noite)
func_nao_carro = set(funcionarios).difference(tem_carro)


print(func_carro_noite)
print(func_carro_dia)
print(func_nao_carro)
