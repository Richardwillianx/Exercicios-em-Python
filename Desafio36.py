"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
tempo = int(input('Informe em quantos anos irá pagar: '))

prest = casa / (tempo * 12)
min = salario * 30/100

print('Para pagar uma casa de R${:.2F} em {} anos.\n A prestação será de R${:.2f}'.format(casa, tempo, prest))

if prest <= min:
    print('empréstimo aprovado')
else:
    print('empréstimo negado.')
