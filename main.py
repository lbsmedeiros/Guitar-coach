"""
1 - Log in
2 - Verificar se é o primeiro login
2.1 - Se for o primeiro login, atestar conhecimento do usuário. Conhecer usuário.
        - O que ele já sabe (haverá um banco de dados contendo os nomes das matérias separadas por módulos)
        - Musicas que já conhece para compor repertório de prática
2.2 - Caso não seja o primeiro login, perguntar se aprendeu algo novo.
3 - Iniciar o programa.
"""

from random import randint, choice, choices
import modulos

escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B',
                    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

