#!/bin/python3

import sys
sys.setrecursionlimit(4000)

def passwordCracker(passwords, attempt):
    # Complete this function
    set_passwords = set(passwords)
    failed = set()

    def helper(attempt):
        if attempt == "":
            return []
        if attempt in failed:
            return "WRONG PASSWORD"

        for i in range(1, len(attempt) + 1):
            if attempt[:i] in set_passwords:
                next = helper(attempt[i:])
                if next != "WRONG PASSWORD":
                    return [attempt[:i]] + next

        failed.add(attempt)
        return "WRONG PASSWORD"

    result = helper(attempt)
    if result == "WRONG PASSWORD":
        return "WRONG PASSWORD"
    else:
        return " ".join(result)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passwords = input().strip().split(' ')
        attempt = input().strip()
        result = passwordCracker(passwords, attempt)
        print(result)
