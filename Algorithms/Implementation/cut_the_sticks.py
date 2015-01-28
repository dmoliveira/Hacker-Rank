#!/usr/bin/env python
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    number_list = sorted(map(int, sys.stdin.readline().split()))

    while number_list:
        print(len(number_list))
        number_list = [number - number_list[0] for number in number_list if number > number_list[0]]