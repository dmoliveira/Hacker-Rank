#!/usr/bin/env python
import sys

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        vector = list(map(int, sys.stdin.readline().split()))
        
        exists_same_sum = 'NO'
        for index in range(1, len(vector)-1):
            if sum(vector[:index]) == sum(vector[index+1:]):
                exists_same_sum = 'YES'
                break
                
        print(exists_same_sum)