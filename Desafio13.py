"""
Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário com 15% de aumento.
"""
salario = float(input('Informe o seu salário R$ '))
aumento = salario + (salario * 15/100)
print('Com o aumento de 15% o funcinário que recebia {:.2f} reais comecará receber {:.2f}'.format(salario, aumento))
