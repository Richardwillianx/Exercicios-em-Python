"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

ex palíndromo: Apos a Sopa.
            A sacada da casa
            A torre da derrota
            O Lobo ama o Bolo.
            (Frases que são a mesma coisa de trás para frente)
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

"""inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
