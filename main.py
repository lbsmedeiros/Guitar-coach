from modulos import Coatch, escala_cromatica, estados, formacoes
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
        escolha4 = input('Tríade ou tétrade: ')
        formacao = formacoes.index(escolha4)

    else:
        tom = randint(0, 11)
        estado = randint(0, 3)
        formacao = randint(0, 1)

    coatch = Coatch(tom, estado, formacao, tempo=10)
    coatch.run()
