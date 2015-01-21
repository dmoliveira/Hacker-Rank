for _ in range(int(input())):
    print ([math.sqrt(number).is_integer() for number in range(a, b+1)].count(True))
