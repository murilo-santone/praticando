from math import sqrt, ceil, floor
import random

num = int(input('Digite um número: '))

raiz = sqrt(num)
print('arredonda pra cima')
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('arredonda pra baixo')
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

print('numero aleatorio de 0 a 1')
num2 = random.random()
print(num2)
print('numero aleatorio de 0 a 10')
num3 = random.randint(1, 10)
print(num3)