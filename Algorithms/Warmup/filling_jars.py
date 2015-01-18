# Python 3!
import math
n,m = map(lambda value: int(value), input().split())
jar_total_sum = 0.0

for _ in range(m):
    a, b, k = map(lambda value: int(value), str(input()).split())
    jar_total_sum += (b-a+1)*k

average_candies = int(math.floor(jar_total_sum/n))
print (average_candies)
import math
n,m = map(lambda value: int(value), raw_input().split())
jar_counter_list = [0]*n

for _ in range(m):
    for value in raw_input().split():
        a, b, k = value
        for jar_index in range(a, b):
            jar_counter_list[jar_index] += k

average_candies = int(math.floor(sum(jar_counter_list)/float(n)))
print average_candies

