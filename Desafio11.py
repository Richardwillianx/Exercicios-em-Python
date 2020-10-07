"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
print()
area = largura * altura
print('Com {:.2f} de largura e {:.2f} de altura, sua parede possui uma aréa de {}m².'.format(largura, altura, area))
print()
tinta = area / 2
print('É necessário {:.2f}L de tinta para pinta-lá.'.format(tinta))
