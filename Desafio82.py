""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

num = list()
par = list()
ímpar = list()
while True:
    num.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        ímpar.append(v)
print('=*'*25)
print(f'A lista completa: {num}')
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {ímpar}')
print('=*'*25)
