"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input('Informe a quantidade de dias que ele foi alugado: '))
km = float(input('Informe a quantidade de KM percorridos: '))

total = (dias * 60) + (km * 0.15)
print()
print('Você deverá pagar R${:.2f} por {:.0f} dias de aluguel do carro e por {:.0f}KM rodados.'.format(total, dias, km))
