""" Faça um programa que leia nome e peso de várias pessoas, guardando tu do em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = list()
dados = list()
maiorp = menorp = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if len(dados) == 0:
        maiorp = menorp = pessoas[1]
    else:
        if pessoas[1] > maiorp:
            maiorp = pessoas[1]
        if pessoas[1] < menorp:
            menorp = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print()
print('=*'*25)

print(f'Ao todo foram cadastradas {len(dados)} pessoas.')

print(f'O maior peso foi de {maiorp}Kg. Peso de ', end='')
for p in dados:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso foi de {menorp}Kg. Peso de ', end='')
for p in dados:
    if p[1] == menorp:
        print(f'[{p[0]}]', end='')
print()
print('=*'*25)
print(f'{"FIM DO PROGRAMA ":^40}')
print('=*'*25)
