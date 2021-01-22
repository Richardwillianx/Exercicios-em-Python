""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """
from datetime import datetime

dados = dict()

dados['nome'] = str(input('Informe se nome: '))
nasc = int(input('Informe seu ano de nascimento: '))

dados['idade'] = datetime.now().year - nasc

dados['ctps'] = int(input('Informe o número da sua CTPS[0 = não possui]: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Informe seu ano de contratação: '))
    dados['salário'] = float(input('Informe o seu salário R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('=-'*30)
for k, v in dados.items():
    print(f' {k} = {v}')