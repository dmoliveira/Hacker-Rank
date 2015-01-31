import sys

if __name__ == '__main__':
    N,T = map(int, sys.stdin.readline().split())
    LANE = list(map(int, sys.stdin.readline().split()))
    
    for _ in range(T):
        i,j = map(int, sys.stdin.readline().split())
        print(min(LANE[i:j+1]))