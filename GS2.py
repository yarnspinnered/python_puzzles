# Complete the function below.

def countSteps(n):
    res = [0] * max(4, n + 1)
    res[1] = 1
    res[2] = 2
    res[3] = 4

    if n <= 3:
        return res[n]

    for i in range(4, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]

for x in range(6):
    print(countSteps(x))