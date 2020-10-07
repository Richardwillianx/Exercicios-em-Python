"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.(ordem de precedência)
"""
nota01 = float(input('Informe a primeira nota: '))
nota02 = float(input('Informe a segunda nota: '))
media = (nota01 + nota02) / 2
print('O aluno recebeu {} e {} ficando com média de {}'.format(nota01, nota02, media))
