"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O Programa deverá na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
pc = randint(0, 5)#Fazendo o pc "pensar".
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('em que número eu pensei? '))#Jogador tentando adivinhar o número.

print('PROCESSANDO . . .')
sleep(2)

print('pensei em {}'.format(pc))

if jogador == pc:
    print('Acertou mizeravi!')
else:
    print('You lose! \n'
          'tente novamente HAHAHAHA')