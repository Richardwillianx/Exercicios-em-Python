"""
Faça um programa que leia uma frase pelo teclado e mostre:
-> Quantas vezes aparece a letra "a".
-> Em que posição ela aparece a primeira vez.
-> Em que posição ela aparece a ultima vez.
"""
frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez que a letra "a" apareceu foi na posição {}.'.format(frase.find('A')+1))
print('A ultima vez que a letra "a" apareceu foi na posição {}.'.format(frase.rfind('A')+1))
