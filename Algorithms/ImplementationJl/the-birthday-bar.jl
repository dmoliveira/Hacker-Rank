# https://www.hackerrank.com/challenges/the-birthday-bar/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

n = numbers()[1]
values = numbers()
d,m = numbers()

count = 0

for i=1:n-m+1
    agg = 0
    j=i
    while j < i+m && agg < d
        agg += values[j]
        j += 1
    end
    agg == d && j == i+m && (count += 1)
end
println(count)
