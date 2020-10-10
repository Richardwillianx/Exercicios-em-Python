"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.

"""
velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade >= 80:
    print('Você foi multado, excedeu o limite que é de 80km/h!')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar uma multa de R${:.2f}'.format(multa))

else:
    print('tenha um ótimo dia, dirija com segurança!')
