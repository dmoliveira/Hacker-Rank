for _ in xrange(input()):
    original_number = input()
    count_list = map(lambda number: 1 if number != '0' and original_number % int(number) == 0 else 0, list(str(original_number)))
    print sum(count_list)
