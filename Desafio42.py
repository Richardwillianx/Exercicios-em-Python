"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais.
- Isósceles: dois lados iguais
- Escaleno: Todos os lados diferentes.
"""

ps = float(input('Informe o primeiro segmento: '))
ss = float(input('Informe o segundo segmento:  '))
ts = float(input('Informe o terceiro segmento: '))

if ts < ss + ts and ss < ps + ss and ts < ps + ss:
    print('Os segmentos PODEM FORMAR um triângulo', end='')
    #if ps == ss == ts:
    if ps == ss and ss == ts:
        print('EQUILÁTERO!')
    #if ps != ss != ts != ps:
    if ps != ss and ss != ts and ts != ps:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
  print('Os segmentos NÃO FORMAM um triângulo.')
