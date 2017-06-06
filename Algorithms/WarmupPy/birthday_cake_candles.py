#!/bin/python3

int(input().strip())
height = list(map(int, input().split(' ')))
height.sort(reverse=True)
max_height = height[0]
count = 1
for u in height[1:]:
    if u != max_height:
        break
    count += 1
print(count)
