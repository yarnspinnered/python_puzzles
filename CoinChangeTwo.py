#!/bin/python3

import sys

def getWays(n, c):
    if len(c) == 0:
        return 0
    res = [([0] * len(c))  for x in range(n + 1)]
    res[0] = [1] * len(c)
    for interm in range(1, n + 1):
        for i in range(len(c)):
            if i > 0:
                res[interm][i] += res[interm][i-1]

            coin = c[i]
            if coin > interm:
                continue

            if interm - coin >= 0:
                res[interm][i] += res[interm - coin][i]

    return res[n][-1]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)