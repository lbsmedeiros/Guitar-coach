"""
1 - Log in
2 - Verificar se é o primeiro login
2.1 - Se for o primeiro login, atestar conhecimento do usuário. Conhecer usuário.
        - O que ele já sabe (haverá um banco de dados contendo os nomes das matérias separadas por módulos)
        - Musicas que já conhece para compor repertório de prática
2.2 - Caso não seja o primeiro login, perguntar se aprendeu algo novo.
3 - Iniciar o programa.
"""

import modulos
from random import randint

if __name__ == '__main__':
    escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    estados = ['Maior', 'Menor Natural', 'Menor Harmônico', 'Menor Melódico']

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

    a = modulos.Escalas(tom, estado)
    print(a.maior())
    print(a.menor_natural())
    print(a.menor_harmonica())
    print(a.menor_melodica())
    print(f'Aquecimento: {a.aquecimento()}')
