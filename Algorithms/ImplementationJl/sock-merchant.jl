# https://www.hackerrank.com/challenges/sock-merchant/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))
n = numbers()[1]
colors = numbers()
pairs = 0
mem = Dict()
for c in colors
    if haskey(mem, c)
        mem[c] += 1
    else
        mem[c] = 1
    end
    if mem[c] % 2 == 0
        pairs += 1
    end
end
println(pairs)
