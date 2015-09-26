# -*- coding: utf-8 -*-

from itertools import combinations_with_replacement


class JugandoConPiedras(object):
    def solve(self, cantidad_piedras):
        cantidad_piedras = int(cantidad_piedras)
        iterable = range(cantidad_piedras + 1)
        comb = (c for c in combinations_with_replacement(iterable,
                                                         cantidad_piedras)
                if sum(c) == cantidad_piedras)
        comb_len = sum(1 for x in comb)
        return (10 ** 9 + 7) % comb_len


if __name__ == '__main__':
    import sys

    jcp = JugandoConPiedras()
    print(jcp.solve(sys.argv[1]))
