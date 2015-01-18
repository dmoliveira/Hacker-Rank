def generate_fibo(size):
    fibo = [0,1]
    start_index = len(fibo)
    for _ in xrange(size-start_index):
       fibo.append(fibo[_ + start_index - 2] + fibo[_ + start_index - 1])
    return fibo

fibo = generate_fibo(10**5)
for _ in xrange(input()):
   print 'IsFibo' if input() in fibo else 'IsNotFibo'
