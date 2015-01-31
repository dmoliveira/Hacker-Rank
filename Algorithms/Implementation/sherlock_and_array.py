import sys

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        vector = list(map(int, sys.stdin.readline().split()))
        exists_same_sum = 'NO'
        if n > 2:
            a = sum(vector[:1])
            b = sum(vector[2:])
        
            for index in range(1, len(vector)-1):
                if a == b:
                    exists_same_sum = 'YES'
                    break
                    
                a += vector[index]
                b -= vector[index+1]
            print(exists_same_sum)
        elif n == 1:
            print('YES')
        else:
            print('NO')