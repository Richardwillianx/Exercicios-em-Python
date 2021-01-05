"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
resp = 'S'
num = med = soma = cont = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? ')).upper().strip()[0]
med = soma / cont
print(f'Você digitou {num} números e a média foi {med}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
