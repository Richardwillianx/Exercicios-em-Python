"""
Crie um program que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print('-='*14)
print('Computador jogou {}'.format(itens[pc]))
print('Você escolheu {}'.format(itens[jogador]))
print('-='*14)

if pc == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')

elif pc == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCEU')


elif pc == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    if jogador == 2:
        print('EMPATE')
