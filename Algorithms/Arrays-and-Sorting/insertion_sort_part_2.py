#!/usr/bin/env python
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    if N == 0:
        print('')
    
    V = list(map(int, sys.stdin.readline().split()))
    
    if N == 1:
        print(V[0])

    for i in range(1, N):
        key = V[i]
    
        j = i-1
        for _ in range(0, i):
            if V[j] > key:
                V[j+1] = V[j]
            else:
                break
            j -= 1
            
      
        V[j+1] = key       
        print(' '.join(map(str,V)))
    