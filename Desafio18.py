"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math
an = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))

cos = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))

tan = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))
