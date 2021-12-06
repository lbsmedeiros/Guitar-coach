from random import choices
from itertools import accumulate, permutations
from operator import mod
from typing import List

escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
estados = ['Maior', 'Menor Natural', 'Menor Harmônico', 'Menor Melódico']
formacoes = ['triade', 'tetrade']
campos_harmonicos_triades = {
    'Maior': ['M', 'm', 'm', 'M', 'M', 'm', 'm(b5)', 'M'],
    'Menor Natural': ['m', 'm(b5)', 'M', 'm', 'm', 'M', 'M', 'm'],
    'Menor Melódico': ['m', 'm(b5)', '(#5)', 'm', 'M', 'M', 'm(b5)', 'm'],
    'Menor Harmônico': ['m', 'm', '(#5)', 'M', 'M', 'm(b5)', 'm(b5)', 'm']
}
campos_harmonicos_tetrades = {
    'Maior': ['7M', 'm7', 'm7', '7M', '7', 'm7', 'm7(b5)', '7M'],
    'Menor Natural': ['m7', 'm7(b5)', '7M', 'm7', 'm7', '7M', '7', 'm7'],
    'Menor Melódico': ['m7M', 'm7', '7M(5#)', '7', '7', 'm7(b5)', 'm7(b5)', 'm7M'],
    'Menor Harmônico': ['m7M', 'm7(b5)', '7M(5#)', 'm7', '7', '7M', 'm7m(b5)', 'm7M']
}


def preencher_escala(passos):
    return [escala_cromatica[mod(passo, 12)] for passo in passos]


def steps(tom, steps):
    return list(accumulate([tom, *steps], lambda x, y: x + y))


class Coatch:
    def __init__(self, tom, estado, formacao, tempo):
        self.tom = tom
        self.estado = estado
        self.formacao = formacao
        self.tempo = tempo

    def alongamento(self):
        return 'Alongue os músculos dos dedos, mãos e braços por 1 minuto. É importante.'

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

    def campo_harmonico(self):
        if self.formacao == 0:
            complemento = campos_harmonicos_triades[estados[self.estado]]
        elif self.formacao == 1:
            complemento = campos_harmonicos_tetrades[estados[self.estado]]
        if self.estado == 0:
            lista = self.maior()
        elif self.estado == 1:
            lista = self.menor_natural()
        elif self.estado == 2:
            lista = self.menor_harmonica()
        elif self.estado == 3:
            lista = self.menor_melodica()
        campo_lista = [f'{x}{y}' for num1, x in enumerate(lista) for num2, y in enumerate(complemento) if num1 == num2]
        campo_string = ' - '.join(campo_lista)
        return campo_string

    def run(self):
        if self.tempo == 10:
            print(self.alongamento())
            print(
                f'Hoje trabalharemos sobre o campo harmônico de {escala_cromatica[self.tom]} {estados[self.estado]} em {formacoes[self.formacao]}'
            )
            print(self.campo_harmonico())
