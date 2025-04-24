def alinhanome():
    nome = input('Qual é o seu nome? ')
    print('Prazer te conhecer {:20}!'.format(nome)) # alinhamento esquerdo
    print('Prazer te conhecer {:>20}!'.format(nome)) # alinhamento direito
    print('Prazer te conhecer {:<20}!'.format(nome)) # alinhamento esquerdo explicito
    print('Prazer te conhecer {:^20}!'.format(nome)) # alinhamento centralizado
    print('Prazer te conhecer {:=^20}!'.format(nome)) # alinhamento centralizado com ' = ' do lado do nome
    return

def umvalor():
    n1 = int(input('Um valor: '))
    n2 = int(input('Outro valor: '))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2
    print('A soma é {}, \n o produto é {} e a \n divisão é {}'.format(s, m, d), end=' >>> ')
    print('Divisão inteira {} e potência {}'.format(di, e))

if __name__ == "__main__":
    alinhanome()
    umvalor()