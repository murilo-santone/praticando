"""
Faça um algoritmo que leia o salário e
mostre seu novo salário, com 15% de aumento.
"""

s = float(input('Informe o salário: '))
aumento = s+(s*15/100)
print('Salário era R$:{:.2f} com aumento de 15% fica R$:{:.2f}'.format(s,aumento))