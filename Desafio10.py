"""
Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (US$ 1,00 = R$ 5,64(cotação atual)
"""
din = float(input('Informe quanto você tem na carteira? R$ '))
dolar = din / 5.65
print('Com {} reais é possível comprar {:.2f} dólares.'.format(din, dolar))
