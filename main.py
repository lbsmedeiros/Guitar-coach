from modulos import Escalas, escala_cromatica, estados
from random import randint

if __name__ == '__main__':
    escolha1 = int(input('Escolher tom ou sortear [ 1 / 2 ]: '))

    if escolha1 == 1:
        escolha2 = input('Selecione o tom desejado: ')
        # Será botão mas aqui, para teste, devemos escrever o tom, exemplo 'D#' (sem aspas)
        tom = escala_cromatica.index(escolha2)
        escolha3 = input(f'Selecione o estado desejado para o tom {escolha2}: ')
        # Também será botão mas aqui, use 'Maior', 'Menor Natural', 'Menor Harmônico' ou 'Menor Melódico'
        estado = estados.index(escolha3)
    else:
        tom = randint(0, 11)
        estado = randint(0, 3)

    a = Escalas(tom, estado)
    print(a.maior())
    print(a.menor_natural())
    print(a.menor_harmonica())
    print(a.menor_melodica())
    print(f'Aquecimento: {a.aquecimento()}')
