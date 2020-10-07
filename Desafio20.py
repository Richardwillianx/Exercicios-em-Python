"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
#import random

print('Informe o nome dos alunos.')

a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
#random.shuffle(lista)
shuffle(lista)

print('Está será a ordem de apresentação.')
print(lista)
