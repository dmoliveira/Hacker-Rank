#!/bin/python
from __future__ import division
import sys


n = int(raw_input().strip())
vector = [0, 0, 0]
for v in map(int,raw_input().strip().split(' ')):
    if v > 0:
        vector[0] += 1
    elif v < 0:
        vector[1] += 1
    else:
        vector[2] += 1

print vector[0]/n
print vector[1]/n
print vector[2]/n
