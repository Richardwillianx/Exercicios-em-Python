"""
Crie um programa que leia duas notas de um aluno e calcule sua média, monstrando no final, de acordo com a média atingida.

- Média abaixo de 5.0: 'Reprovado'
- Média entre 5.0 e 6.9: 'Recuperação'
- Média 7.0 ou superior: 'Aprovado'.
"""

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
média = (nota1 + nota2) / 2
print()
print('Com as notas de {:.1f} e {:.1}, a sua média é {:.1f}.'.format(nota1, nota2, média))

if média < 5.0:
    print('Você foi reprovado.')
elif média >= 5.0 and 6.9:
    print('Você está de recuperação.')
elif média >= 7.0:
    print('Você foi aprovado, PARABÉNS!')
