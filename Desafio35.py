"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))
print()
if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print('Os segmentos acima FORMAM um triângulo.')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo.')
