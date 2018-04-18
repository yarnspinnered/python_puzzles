#!/bin/python3

import sys

def equal(arr):
    # Complete this function
    res = [0] * 3
    original_min = min(arr)
    for i in range(3):
        target = original_min - i
        arr_c = arr[:]
        for j in range(len(arr_c)):
            while arr_c[j] > target:
                if arr_c[j] >= target + 5:
                    number_of_fives = (arr_c[j] - target)//5
                    arr_c[j] -= number_of_fives * 5
                    res[i] += number_of_fives
                elif arr_c[j] >= target + 2:
                    arr_c[j] -= 2
                    res[i] += 1
                elif arr_c[j] == target + 1:
                    arr_c[j] -= 1
                    res[i] += 1
    return min(res)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = equal(arr)
        print(result)
