# -*- coding: utf-8 -*-


class IslaDelTesoro(object):
    def solve(self, alturas):
        estado = (0, 0)
        estado_final = (len(alturas) - 1, len(alturas[0]) - 1)
        cant_filas = len(alturas)
        cant_columnas = len(alturas[0])
        coordenadas = [(x, y)
                       for x in range(cant_filas)
                       for y in range(cant_columnas)]
        tiempo = 0

        while estado != estado_final:
            siguientes = self.get_vecinos_estado(estado[0], estado[1], coordenadas)
            siguientes_val = [alturas[coord[0]][coord[1]]
                              for coord in siguientes]
            indice = siguientes_val.index(max(siguientes_val))
            estado = siguientes[indice]
            tiempo += 1

            if estado_final in siguientes:
                break

        resultado = alturas[-1][-1] - tiempo - 1
        return -1 if not resultado else resultado

    def get_vecinos_estado(self, x, y, coordenadas, iterate=False):
        vecinos = []
        vappend = vecinos.append

        for fila, columna in ((x + i, y + j)
                              for i in (-1, 0, 1) for j in (-1, 0, 1)
                              if i != 0 or j != 0):
            if (fila, columna) in coordenadas and ((fila == x) or (columna == y)):
                vappend((fila, columna))
        if iterate:
            return iter(vecinos)
        else:
            return vecinos
