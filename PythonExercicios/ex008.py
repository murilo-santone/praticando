"""
Escreva um programa que leia um valor em metros e a
exiba convertido em centímetros e milímetros
"""

m = float(input('Digite seu valor em metros: '))

print('Convertido em centímetros: {:.2f}'.format(m*100))
print('Convertido em milímetros: {:.2f}'.format(m*1000))