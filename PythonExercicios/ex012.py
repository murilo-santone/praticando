"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Informe o preço do produto: '))
d = 0.05/p
print('O produto com 5% de desconto fica: {:.2f}'.format(p-d))