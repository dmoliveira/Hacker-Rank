#!/bin/python3
def solve(grade):
    if grade < 38:
        return grade
    return grade//5*5+5 if grade % 5 >= 3 else grade

n = int(input().strip())
print("\n".join([
    str(solve(int(input().strip())))
    for _ in range(n)
]))

