"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milímetros.
"""
metros = float(input('Informe um número: '))
cm = metros * 100
mm = metros * 1000
print('{}metros corresponde a {:.0f} e a {:.0f}'.format(metros, cm, mm))
