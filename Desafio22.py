"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas.
-> O nome com todas as letras minúsculas.
-> Quantas letras ao todo (sem considerar espaços)
-> Quantas letras tem o primeiro nome.
"""

nome = str(input('Informe seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome com todas letras maiúsculas ficará: {}.'.format(nome.upper()))
print('Seu nome com todas letras minúsculas ficará: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(lista[0], nome.find(' ')))
