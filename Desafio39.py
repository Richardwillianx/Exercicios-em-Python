"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele 'ainda vai se alistar' ao serviço militar.
- Se é a 'hora de se alistar'.
- Se já 'passou do tempo' do alistamento.

Seu programa também deverá mostra o tempo que falta ou que passou do prazo.
"""
from datetime import date
atual = date.today().year
ano = int(input('Informe o ano que você nasceu: '))

idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda falta {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
