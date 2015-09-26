# -*- coding: utf-8 -*-

from __future__ import division


class BocaDeUrna(object):
    def solve(self, votos_obtenidos):
        cantidad_votos_total = sum(votos_obtenidos)
        cant_votos_1st = max(votos_obtenidos)
        porcentaje_votos_ganador = cant_votos_1st * 100 / cantidad_votos_total

        votos_obtenidos_copy = votos_obtenidos[:]
        votos_obtenidos_copy.remove(cant_votos_1st)
        cant_votos_2nd = max(votos_obtenidos_copy)
        porcentaje_votos_segundo = cant_votos_2nd * 100 / cantidad_votos_total

        test_1 = porcentaje_votos_ganador >= 45
        test_2 = porcentaje_votos_ganador >= 40
        test_3 = test_2 and \
            porcentaje_votos_ganador - porcentaje_votos_segundo >= 10

        vuelta = 1 if test_1 or test_3 else 2

        return vuelta
