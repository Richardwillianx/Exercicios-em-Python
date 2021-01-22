""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. """

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)

    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r == 'N':
        break

print('=*'*25)
print(f'Foram adicionado {len(lista)} elementos.')

print(f'Os valores em forma decrescente {lista}')

if 5 in lista:
    print('O número 5 foi adicionado a lista')
else:
    print('O valor 5 NÃO foi adicionado a lista.')

print('=*'*25)