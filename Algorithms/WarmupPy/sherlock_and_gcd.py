for _ in range(int(input())):
    n = int(input())
    values = sorted(map(lambda value: int(value), (input().split())))
    divisors = map(lambda number: number, range(2, values[-1]+1))

    for divisor in divisors:
        count = [1 for value in values if value % divisor == 0].count(1)
        if count == n:
            break
    
    print('NO') if count == n else print('YES')