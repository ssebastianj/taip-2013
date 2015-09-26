# -*- coding: utf-8 -*-

from solution import JugandoConPiedras


class TestJugandoConPiedras(object):
    @classmethod
    def setup_class(cls):
        cls.jcp = JugandoConPiedras()

    def test_solve(self):
        assert self.jcp.solve(4) == 2
        assert self.jcp.solve(239) == 465766207
