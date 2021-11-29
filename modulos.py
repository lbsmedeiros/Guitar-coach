from random import choices
from itertools import accumulate, permutations
from operator import mod
from typing import List


escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
estados = ['Maior', 'Menor Natural', 'Menor Harmônico', 'Menor Melódico']


def campo_harmonico(tom, estado):
    coatch = Coatch(tom, estado)
    if estado == 0:
        lista = coatch.maior()
        campo = ''
        for i, nota in enumerate(lista):
            if i == 0:
                campo += f'{nota}'
            else:
                campo += f' - {nota}'
        return campo
    elif estado == 1:
        lista = coatch.menor_natural()
        campo = ''
        for i, nota in enumerate(lista):
            if i == 0:
                campo += f'{nota}'
            else:
                campo += f' - {nota}'
        return campo
    elif estado == 2:
        lista = coatch.menor_harmonica()
        campo = ''
        for i, nota in enumerate(lista):
            if i == 0:
                campo += f'{nota}'
            else:
                campo += f' - {nota}'
        return campo
    elif estado == 3:
        lista = coatch.menor_melodica()
        campo = ''
        for i, nota in enumerate(lista):
            if i == 0:
                campo += f'{nota}'
            else:
                campo += f' - {nota}'
        return campo


def preencher_escala(passos):
    return [escala_cromatica[mod(passo, 12)] for passo in passos]


def steps(tom, steps):
    return list(accumulate([tom, *steps], lambda x, y: x + y))


class Coatch:
    def __init__(self, tom, estado):
        self.tom = tom
        self.estado = estado

    def alongamento(self):
        return 'Alongue os músculos dos dedos, mãos e braços por 1 minuto. É importante.'

    def maior(self: int) -> List[str]:
        passos = steps(self.tom, [2, 2, 1, 2, 2, 2, 1])
        return preencher_escala(passos)

    def menor_natural(self: int) -> List[str]:
        passos = steps(self.tom, [2, 1, 2, 2, 1, 2, 2])
        return preencher_escala(passos)

    def menor_harmonica(self: int) -> List[str]:
        passos = steps(self.tom, [2, 1, 2, 2, 1, 3, 1])
        return preencher_escala(passos)

    def menor_melodica(self: int) -> List[str]:
        passos = steps(self.tom, [2, 1, 2, 2, 2, 2, 1])
        return preencher_escala(passos)

    def aquecimento(self):
        possibilidades = list(permutations((1, 2, 3, 4), ))
        resultado = choices(possibilidades, k=2)
        final = ''
        for i, a in enumerate(resultado):
            if i == 0:
                for j, b in enumerate(a):
                    if j == 0:
                        final += str(b)
                    else:
                        final += f'-{str(b)}'
            else:
                final += ' / '
                for j, b in enumerate(a):
                    if j == 0:
                        final += str(b)
                    else:
                        final += f'-{str(b)}'
        return final

    def run(self, tempo: int):
        if tempo == 10:
            self.alongamento()
