#!/bin/python3
import sys

n = int(input().strip())
string = ""
for i in range(n):
    string += " " * (n-(i+1)) +  "#" * (i+1) + "\n"
print(string)
