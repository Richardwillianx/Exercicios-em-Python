"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint

pc = randint(0, 10)
print('\033[31mSou seu computador.. Acabei de pensar em um número entre 0 e 10.\033[m')

print('=*'*20)
print('\033[32mSerá que você consegue adivinhar?\033[m')
print('=*'*20)

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[33mQual é o seu palpite?\033[m '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('\033[31m mais.. tente novamente.\033[m')
        elif jogador > pc:
            print('\033[35m menos, tente novamente.\033[m')
print()
print(f'\033[7m Acertou com {int(palpites)} palpites!')
