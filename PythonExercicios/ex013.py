"""
Faça um algoritmo que leia o salário e
mostre seu novo salário, com 15% de aumento.
"""

s = float(input('Informe o salário: '))
aumento = 0.15*s
print('Salário com aumento de 15% fica: {:.2f}'.format(s+aumento))