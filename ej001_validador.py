from functools import reduce


def validador_tribu_agua(grupos: list[list[int]], b: int):
    coeficiente = sum(list(map(lambda x: sum(x)**2, grupos)))
    return coeficiente <= b
