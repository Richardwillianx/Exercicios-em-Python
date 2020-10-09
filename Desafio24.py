"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
"""
print('Sua cidade possui "santo" no nome?')
cidade = str(input('Informe o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')


