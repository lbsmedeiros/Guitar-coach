from random import choices
from itertools import accumulate, permutations
from operator import mod
from typing import List

escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
estados = ['Maior', 'Menor Natural', 'Menor Harmônico', 'Menor Melódico']


def preencher_escala(passos):
    return [escala_cromatica[mod(passo, 12)] for passo in passos]


class Escalas:
    def __init__(self, tom, estado):
        self.tom = tom
        self.estado = estado

    def maior(self: int) -> List[str]:
        passos = list(accumulate([self.tom, 2, 2, 1, 2, 2, 2, 1], lambda x, y: x + y))
        return preencher_escala(passos)

    def menor_natural(self: int) -> List[str]:
        passos = list(accumulate([self.tom, 2, 1, 2, 2, 1, 2, 2], lambda x, y: x + y))
        return preencher_escala(passos)

    def menor_harmonica(self: int) -> List[str]:
        passos = list(accumulate([self.tom, 2, 1, 2, 2, 1, 3, 1], lambda x, y: x + y))
        return preencher_escala(passos)

    def menor_melodica(self: int) -> List[str]:
        passos = list(accumulate([self.tom, 2, 1, 2, 2, 2, 2, 1], lambda x, y: x + y))
        return preencher_escala(passos)

    def aquecimento(self):
        possibilidades = list(permutations((1, 2, 3, 4),))
        return choices(possibilidades, k=2)


# Testes
if __name__ == '__main__':
    a = Escalas(0, 3)
    print(a.maior())
    print(a.menor_natural())
    print(a.menor_harmonica())
    print(a.menor_melodica())
    print(f'Aquecimento: {a.aquecimento()}')
