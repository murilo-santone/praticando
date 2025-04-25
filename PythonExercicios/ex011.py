"""
Faça um programa que leia a largura e a
altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m².
"""

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede:  '))

area = largura*altura

tinta = area/2

print('Área da parede: {:.3f}m2'.format(area))
print('Você precisa de {:.4f} litros de tinta para pintar sua parede'.format(tinta))