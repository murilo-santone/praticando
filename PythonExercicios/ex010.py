"""
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.

Considerar
US$1,00=RS3,27
"""

dolar = 3.27
carteira = float(input('Quanto você tem na carteira? '))

print('Você pode comprar {:.2f} dólares'.format(carteira/dolar))