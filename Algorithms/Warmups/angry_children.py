import math

def count_modifications(token):
    
    count = 0 
    index_middle = int(math.floor(len(token)/2.0))
    token = token.lower()
    
    for index in range(index_middle):
        count += abs(ord(token[index]) - ord(token[len(token)-1-index]))

    return count

for _ in xrange(input()):
    print count_modifications(raw_input())
