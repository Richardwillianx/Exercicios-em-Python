"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00 , calcule aumenteo de 10%.
Pra os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Informe o seu salário: R$'))

if salario <= 1.250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem recebia R${:.2f} comecará receber R${:.2f}'.format(salario, novo))
