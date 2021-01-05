"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
print('=*'*15)
print(f'\033[31mVAMOS JOGAR PAR OU ÍMPAR?\033[m')
print('=*'*15)
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador {pc}. Total de {total}.', end=' ')
    print('Deu PAR.'if total % 2 == 0 else 'Deu ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mVocê VENCEU!\033[m')
            v += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[32mVOCÊ VENCEU\033[m')
            v += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    print('Vamos jogar novamente..')
print(f'GAME OVER! Você venceu {v} vezes. ')
