"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""
celsius = float(input('Informe a temperatura em Celsius: '))
fah = ((celsius * 9)/5) + 32
print('{:.0f}ºC corresponde a {:.0f}ªF'.format(celsius, fah))
