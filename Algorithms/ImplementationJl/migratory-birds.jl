numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

n = numbers()[1]
values = numbers()

counts = fill(0, 5)
mostindex = 6
mostcount = 0

for v in values
    counts[v] += 1
    if counts[v] > mostcount || counts[v] == mostcount && v <= mostindex
        mostindex = v
        mostcount = counts[v]
    end
end
println(mostindex)
