"""
Um Professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude , lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice

#import random

print('Informe o nome dos alunos.')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

#escolhido = random.choice(lista)

escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))
