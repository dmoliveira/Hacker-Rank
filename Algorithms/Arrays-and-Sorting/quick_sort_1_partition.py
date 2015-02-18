if __name__ == '__main__':
    n = int(input())
    v = list(map(int, input().split()))
    
    p = v[0]
    del v[0]
    
    left = []; middle=[p]; right = []
    for i in range(len(v)):
        if v[i] < p:
            left.append(v[i])
        elif v[i] > p:
            right.append(v[i])
        else:
            middle.append(v[i])
            
    print (' '.join(map(str, left + middle + right)))
            