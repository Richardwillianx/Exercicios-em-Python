"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual ser a base de conversão:

1 - binário
2 - octal
3 - hexadecimal
"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter pra Hexadecimal''')
print()
opção = int(input('Sua opção: .'))
print()

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('opção inválida, tente novamente.')
