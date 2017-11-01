# https://www.hackerrank.com/challenges/between-two-sets/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

numbers()
A,B = numbers(), numbers()
s,e = maximum(A), minimum(B)

count = 0
for i=1:round(Int, e/s)
    factor = s*i
    count += all(a-> factor % a == 0, A) && all(b-> b % factor == 0, B)? 1 : 0
end
println(count)
