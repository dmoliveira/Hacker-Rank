def count_modifications(token):

    count = 0
    for index, letter in enumerate(list(token)):
        if index > 0 and token[index-1] == letter:
            count += 1
    return count

for _ in xrange(input()):
    print count_modifications(raw_input())
