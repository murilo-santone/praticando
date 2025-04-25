"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Informe o preço do produto: '))
d = p-(p*5/100)
#d = 0.5/p
print('O produto custava R${}, com 5% de desconto fica: R${:.2f}'.format(p,d))