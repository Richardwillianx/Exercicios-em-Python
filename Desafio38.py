"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é 'maior'
- O segundo valor é 'menor'
- Não existe valor maior, os dois são iguais.
"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print('{} é maior'.format(num1))
    print('{} é menor.'.format(num2))
elif num2 > num1:
    print('{} é maior'.format(num2))
    print('{} é menor'.format(num1))
else:
    print('Não existe número maior, os dois são iguais.')
