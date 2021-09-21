from random import randint, choice, choices

cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B',
             'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def maior(tom):
    passos = [2, 2, 1, 2, 2, 2, 1]
    posicao = 0
    escala_maior = []
    while len(escala_maior) < 7:
        escala_maior.append(cromatica[tom])
        tom += passos[posicao]
        posicao += 1
    return escala_maior


def menor_natural(tom):
    passos = [2, 1, 2, 2, 1, 2, 2]
    posicao = 0
    escala_menor_natural = []
    while len(escala_menor_natural) < 7:
        escala_menor_natural.append(cromatica[tom])
        tom += passos[posicao]
        posicao += 1
    return escala_menor_natural


def menor_harmonica(tom):
    passos = [2, 1, 2, 2, 1, 3, 1]
    posicao = 0
    escala_menor_harmonica = []
    while len(escala_menor_harmonica) < 7:
        escala_menor_harmonica.append(cromatica[tom])
        tom += passos[posicao]
        posicao += 1
    return escala_menor_harmonica


def menor_melodica(tom):
    passos = [2, 1, 2, 2, 2, 2, 1]
    posicao = 0
    escala_menor_melodica = []
    while len(escala_menor_melodica) < 7:
        escala_menor_melodica.append(cromatica[tom])
        tom += passos[posicao]
        posicao += 1
    return escala_menor_melodica


if __name__ == '__main__':
    print(f'Escala maior:           \t{maior(0)}')
    print(f'Escala menor natural:   \t{menor_natural(0)}')
    print(f'Escala menor harmonica: \t{menor_harmonica(0)}')
    print(f'Escala menor melódica:  \t{menor_melodica(0)}')
