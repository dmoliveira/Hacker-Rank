T = int(input())

for i in range(T):

    N,C,M = map(lambda value: int(value), str(input()).split())
    
    current_chocolates = int(N/C)
    total_chocolates = current_chocolates
    
    wrappers = current_chocolates
    
    while wrappers >= M:
        current_chocolates = int(wrappers/M)
        total_chocolates += current_chocolates
        wrappers = current_chocolates + (wrappers % M if wrappers >= M else 0)
    
    print(total_chocolates)

