"""
Desenvolva umm programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
"""

d = int(input('Qual é a distância da sua viagem? '))
valor = d * 0.50 if d <= 200 else d * 0.45

"""if d <= 200:
    valor = d * 0.50
else:
    valor = d * 0.45"""

print('Sua viagem custará R${:.2f}'.format(valor))
