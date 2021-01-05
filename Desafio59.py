"""
 Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep
pn = int(input('Informe o primeiro número: '))
sn = int(input('Informe o segundo número: '))
op = 0
while op != 5:
    print('''
    *=ESCOLHA UMA OPÇÃO=*
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        soma = pn + sn
        print(f'A soma entre {pn} e {sn} é igual a {soma}')
    elif op == 2:
        multiplicar = pn * sn
        print(f'A multiplicação entre {pn} e {sn} é igual a {multiplicar}')
    elif op == 3:
        if pn > sn:
            maior = pn
        else:
            maior = sn
        print(f'entre {pn} e {sn} o maior é {maior}')
    elif op == 4:
        print('Informe os números novamente!')
        pn = int(input('Informe o primeiro número: '))
        sn = int(input('Informe o segundo número: '))
    elif op == 5:
        print('Finalizando..')
    else:
        print('Opção inválida, digite novamente.')
    print('*=*'*10)
    sleep(2)
print('Fim do Programa, até a próxima!')
