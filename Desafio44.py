"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- em até 2x nno cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.

"""

print('===== LOJAS RICHARDs =====')
compras = float(input('Qual é o valor das suas compras?R$ '))
print()
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print()
opção = int(input('Qual é a forma de pagamento? '))
if opção == 1:
    total = compras - (compras * 10 / 100)

elif opção == 2:
    total = compras - (compras * 5 / 100)
elif opção == 3:
    total = compras
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = compras + (compras * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(totparc, parcela))
    print('Sua compra será parcelada em ')
else:
    total = compras
    print('\033[31m OPÇÃO INVÁLIDA')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, total))
