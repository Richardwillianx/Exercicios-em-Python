"""
Faça um programa que leia um número de 0 a 9999 e amostre na tela cada um dos digitos separadaos.

ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

num = int(input('Informe um número entre 0 e 9999: '))
#n = str(num)
#print('Analisando o número {}.'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

print('Analisando o número {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))
