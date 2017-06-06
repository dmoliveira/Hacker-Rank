import math
max_value = int(math.sqrt(10**9))
for _ in range(int(input())):
    a,b = map(lambda value: int(value), input().split())
    a = int(math.ceil(math.sqrt(a)))
    b = int(math.floor(math.sqrt(b)))
    print ([1 for number in range(a, b+1)].count(1))
