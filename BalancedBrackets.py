#!/bin/python3

import sys

def isBalanced(s):
    # Complete this function
    stk = []
    closed_brackets = set([")", "}", "]"])
    for bracket in s:
        if stk:
            if stk[-1] == "{" and bracket == "}":
                stk.pop(-1)
            elif stk[-1] == "[" and bracket == "]":
                stk.pop(-1)
            elif stk[-1] == "(" and bracket == ")":
                stk.pop(-1)
            elif bracket in closed_brackets:
                return "NO"
            else:
                stk.append(bracket)
        else:
            stk.append(bracket)

    if stk:
        return "NO"
    else:
        return "YES"
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
