import math
for _ in range(int(input())):
    a,b = map(lambda value: int(value), input().split())
    print ([math.sqrt(number).is_integer() for number in range(a, b+1)].count(True))
