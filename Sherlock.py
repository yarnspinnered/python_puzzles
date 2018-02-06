#!/bin/python3

import sys

def isValid(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    freq_cnt_d = {}

    for val in d.values():
        if val in freq_cnt_d.keys():
            freq_cnt_d[val] += 1
        else:
            freq_cnt_d[val] = 1

    freq_lst = [x for x in freq_cnt_d.keys()]
    if len(freq_lst) <= 1:
        return "YES"
    elif len(freq_lst) == 2:
        if 1 in freq_lst and freq_cnt_d[1] == 1:
            return "YES"
        elif freq_lst[0] + 1 == freq_lst[1]:
            if freq_cnt_d[freq_lst[1]] == 1:
                return "YES"
        elif freq_lst[1] + 1 == freq_lst[0]:
            if freq_cnt_d[freq_lst[0]] == 1:
                return "YES"
    return "NO"
s = input().strip()
result = isValid(s)
print(result)
