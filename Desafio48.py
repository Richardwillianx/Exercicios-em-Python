"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontra entre 1 e 500.
"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f'A soma de todos os {cont} valores solicitados é {soma}.')
