# -*- coding: utf-8 -*-

from solution import IslaDelTesoro


class TestIslaDelTesoro(object):
    @classmethod
    def setup_class(cls):
        cls.idt = IslaDelTesoro()

    def test_solve(self):
        assert self.idt.solve([[2, 3, 4],
                               [3, 4, 5],
                               [4, 5, 6]]) == 1

        assert self.idt.solve([[1, 2, 3],
                               [2, 2, 3],
                               [2, 4, 5]]) == -1

        assert self.idt.solve([[1000, 1000],
                               [1000, 1000],
                               [1000, 314]]) == 310
