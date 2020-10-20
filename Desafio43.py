"""
Desenvolva uma lógica que leia o pessoa e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- 25 até 30: Sobrepeso
- 30 a 40: obesidade.
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Informe o seu peso: (KG)'))
altura = float(input('Informe a sua altura: (m)'))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc <= 25 and imc < 30:
    print('Você está sobrepeso.')
elif imc <= 30 and imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')
