"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
op = 0
list = []
while op == 0:
    nome = str(input("Informe o nome do seu aluno: "))
    list.append(nome)
    op = int(input('Deseja inserir outro nome? (1- não, 0- sim)'))

print(list)
print("O aluno sorteado para apagar o quadro será: {}".format(choice(list)))