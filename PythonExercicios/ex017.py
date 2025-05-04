"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

print('Forma 1')
print("O comprimento da hipotenusa é: {:.2f}".format(math.sqrt(cateto_oposto**2 + cateto_adjacente**2)))
hip = math.hypot(cateto_oposto, cateto_adjacente)
print("O comprimento da hipotenusa é: {:.2f}".format(hip))