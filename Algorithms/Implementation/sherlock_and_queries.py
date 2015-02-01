N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(1, M+1):
    for j in range(1, N+1):
        if not j % B[i-1]:
            A[j-1] *= C[i-1]
            
print(' '.join(list(map(str, A))))

