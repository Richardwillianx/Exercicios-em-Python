"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

v = input('Informe algo: ')
print('O tipo primitivo desse valor é ', type(v))
print('Só tem espaços? ', v.isspace())
print('é um número? ', v.isnumeric())
print('É alfabético? ', v.isalpha())
print('É alfanúmerico? ', v.isalnum())
print('Está em maniúsculas? ', v.isupper())
print('Está em minúsculas? ', v.islower())
print('Está capitalizada? ', v.istitle())
