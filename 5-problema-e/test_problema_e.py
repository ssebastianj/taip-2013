# -*- coding: utf-8 -*-

from solution import EscapeAlEscape


class TestEscapeAlEscape(object):
    @classmethod
    def setup_class(cls):
        cls.eae = EscapeAlEscape()

    def test_solve(self):
        assert self.eae.solve('011101001') == 3
        assert self.eae.solve('100010110011101') == 4
        assert self.eae.solve('11111') == 1
        assert self.eae.solve('00000') == 1
