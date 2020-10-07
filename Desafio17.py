"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hp = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa irá medir {:.2f}!'.format(hp))

"""import math

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

hp = math.hypot(co, ca)

print('A hipotenusa irá medir {:.2f}!'.format(hp))"""


"""from math import hypot

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

hp = hypot(co, ca)

print('A hipotenusa irá medir {:.2f}!'.format(hp))"""
