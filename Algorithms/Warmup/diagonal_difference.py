#!/bin/python

import sys


n = int(raw_input().strip())
total = 0

for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   total += a_temp[a_i] - a_temp[n-(a_i+1)]

print abs(total)
