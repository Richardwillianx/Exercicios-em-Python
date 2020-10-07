"""
Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127.
    O número 6.127 tem a porte inteira 6
"""
#import math
#n = float(input('Informe um número: '))
#print('A porção inteira de {} é {}.'.format(n, math.trunc(n)))

#from math import trunc
#n = float(input('Informe um valor: '))
#print('A porção inteira de {} é {}.'.format(n, trunc(n)))

n = float(input('Informe um número: '))
print('A porção inteira de {} é {}.'.format(n, int(n)))


