"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
        nasc = int(input(f'Em que ano a {c}º pessoa nasceu? '))
        idade = atual - nasc
        if idade >= 21:
            maior += 1
        else:
            menor += 1
print(f'Ao todo temos {maior} pessoas maiores de idade.')
print(f'Ao todo temos {menor} pessoas menor de idade.')
