# -*- coding: utf-8 -*-

from solution import BocaDeUrna


class TestBocaDeUrna(object):
    @classmethod
    def setup_class(cls):
        cls.bdu = BocaDeUrna()

    def test_solve(self):
        assert self.bdu.solve([60, 40]) == 1
        assert self.bdu.solve([16, 28, 21]) == 1
        assert self.bdu.solve([42, 23, 35]) == 2
        assert self.bdu.solve([297, 302, 401]) == 2
