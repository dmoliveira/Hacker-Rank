import random
import sys

def merge(A, p, q, r):
    L = A[p:q] + [sys.maxint]
    R = A[q:r] + [sys.maxint]

    i,j = (0,0)
    
    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A,p,r):
    if p < r-1:
        q = (r+p)/2
        
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    N = 100 
    A = [random.randint(1, N) for _ in range(N)]
    merge_sort(A, 0, N)
    print 'Sorted:',A
