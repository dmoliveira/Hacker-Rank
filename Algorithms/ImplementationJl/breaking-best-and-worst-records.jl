# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

n, scores = numbers()[1], numbers()
counts = [0,0]
least, most = scores[1], scores[1]
for s=scores[2:n]
    if least > s
        counts[1] += 1
        least = s
    end
    if most < s
        counts[2] += 1
        most = s
    end
end
println(counts[2], " ", counts[1])
