"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('GERADOR DE PA')
print('-='*10)
pt = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo}>', end='')
    termo += raz
    cont += 1
print(' FIM')