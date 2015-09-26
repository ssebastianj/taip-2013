# -*- coding: utf-8 -*-


class EscapeAlEscape(object):
    def solve(self, input_log):
        all_ones = all([bool(int(i)) for i in input_log])
        all_zeroes = all([not bool(int(i)) for i in input_log])

        if all_ones or all_zeroes:
            sep_long = 1
        else:
            sep_long = ((len(input_log) // 2) // 2) + 1

        return sep_long
