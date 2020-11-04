"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A média de idade do grupo
    - Qual é o nome do homem mais velho.
    - Quantas mulheres tem menos de 20.
"""
somaidade = 0
média = 0
maiorhomem = 0
nomevelho = ''
mulher20 = 0

for p in range(1, 5):
    print(f'----- {p}º PESSOA------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

média = somaidade / 4
print(f'A média de idade do grupo é de {média} anos')
print(f'O home mais velho tem {maiorhomem} e se chama {nomevelho}')
print(f'Ao todo são {mulher20} com menos de 20 anos.')
