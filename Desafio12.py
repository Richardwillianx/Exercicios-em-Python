"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""
produto = float(input('Informe o valor do produto: R$  '))
novo = produto - (produto * 5/100)
print('Esse produto custa {:.2f} reais com desconto de 5% custará {:.2f} reais.'.format(produto, novo))
