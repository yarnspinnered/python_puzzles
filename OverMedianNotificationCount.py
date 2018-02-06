#!/bin/python3

import sys
import bisect

def activityNotifications(expenditure, d):
    def median(arr):
        m = len(arr) // 2
        if len(arr) % 2 == 0:
            return (arr[m] + arr[m-1])/2
        else:
            return arr[m]

    if d >= len(expenditure):
        return 0
    curr = expenditure[:d]
    curr.sort()
    remove_queue = expenditure[:d]
    alerts = 0
    for i in range(d, len(expenditure)):
        new_val = expenditure[i]
        med = median(curr)
        if new_val >= med * 2:
            alerts += 1
        insertion_point = bisect.bisect_left(curr, new_val)
        curr.insert(insertion_point, new_val)
        removal_point = bisect.bisect_left(curr, remove_queue.pop(0))
        curr.pop(removal_point)
        remove_queue.append(new_val)

    return alerts



if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)
