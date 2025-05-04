"""
O mesmo professor do desafio anterior quer sorter a ordem de
apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random

op = 0
list = []

while op == 0:
    nome = str(input("Informe o nome do aluno: "))
    list.append(nome)
    op = int(input("Deseja inserir outro nome? (0- Sim, 1- Não)"))
    random.shuffle(list)

print("A ordem de apresentação será: {}".format(list))