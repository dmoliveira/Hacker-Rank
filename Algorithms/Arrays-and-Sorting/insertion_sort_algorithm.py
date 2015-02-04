import random
N = 100
vector = [random.randint(1,1000) for _ in range(N)]

for j in range(1, N):
    key = vector[j]
    i = j-1
    while i > 0  and key < vector[i]:
        vector[i+1] = vector[i]
        i -= 1
    vector[i] = key

print(vector) 
