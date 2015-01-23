for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    
    m = n-1
    print(' '.join(map(lambda v: str(v), sorted(set(map(lambda alpha: (m-alpha)*a + (alpha)*b, range(n)))))))