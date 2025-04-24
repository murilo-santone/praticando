"""
Faça um programa que leia um número inteiro qualquer e
mostre na sua tela a sua tabuada.
"""

n = int(input('Digite um número inteiro: '))

tabuada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for t in tabuada:
    print('{} x {:2} = {}'.format(n, t, n*t))
