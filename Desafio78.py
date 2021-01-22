""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.  """

listagem = []
maior = menor = 0
for c in range(0, 5):
   listagem.append(int(input(f'Informe um valor para a posição {c}: ')))
   if c == 0:
       maior = menor = listagem[c]
   else:
    if listagem[c] > maior:
        maior = listagem[c]
    if listagem[c] < menor:
        menor = listagem[c]
print()
print(f'Foram digitados os valores: {listagem}')
print(f'O maior valor é {maior}, na posição ', end='')
for i, v in enumerate(listagem):
    if v == maior:
        print(f'{i}..', end='' )
print()
print(f'O menor valor é {menor}, na posição ', end='')
for i, v in enumerate(listagem):
    if v == menor:
        print(f'{i}..', end='')

#print(f'O maior valor foi : {max(listagem)}')
#print(f'O menor valor foi : {min(listagem)}')
