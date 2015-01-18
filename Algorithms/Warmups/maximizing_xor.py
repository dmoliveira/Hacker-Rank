def find_max(left, right):
    max_xor = 0
    for l in range(left, right+1):
        for r in range(left, right+1):
            if l ^ r > max_xor:
                max_xor = l ^ r

    return max_xor

print find_max(input(), input())
 

