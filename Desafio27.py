"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

ex: Ana Maria de Souza
primeiro: Ana
último: Souza
"""

nome = str(input('Informe o seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é {}.'.format(lista[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
