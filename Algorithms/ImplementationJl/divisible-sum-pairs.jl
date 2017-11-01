# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

n,k = numbers()
A = numbers()

count = 0
for i=1:n, j=i+1:n
    (A[i]+A[j]) % k == 0 && (count += 1)
end
println(count)
