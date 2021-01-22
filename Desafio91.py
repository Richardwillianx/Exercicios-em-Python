"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. """

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador01': randint(1, 6),
        'jogador02': randint(1, 6),
        'jogador03': randint(1, 6),
        'jogador04': randint(1,6)}
ranking = list()
print('=-'*5, 'VALORES SORTEADOS', '=-'*5)
for k, v in jogo.items():
    print(f'O {k} sorteou o número {v}.')
    sleep(1)
print('=-'*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('   === RANKING FINAL === ')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('=-'*20)