calculate_growth_cycle(h,c,m):
    """
       PARAMS
       ------
       h height
       c cycle
       m maximum cycle
    """
    if c > m or m == 0:
        return h
    else:
        if c % 2 == 1:
            h = 2*h
            return calculate_growth_cycle(h,c+1,m)
        else:
            h = h+1
            return calculate_growth_cycle(h,c+1,m)

for _ in xrange(input()):
    print calculate_growth_cycle(1,1,input())
