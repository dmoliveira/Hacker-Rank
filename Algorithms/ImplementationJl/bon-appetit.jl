# https://www.hackerrank.com/challenges/bon-appetit/problem 
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

n,k = numbers()
costs = numbers()
charge = numbers()[1]

totalcosts = sum(costs)
annacharge = round(Int, (totalcosts-costs[k+1])/2)
println(annacharge == charge? "Bon Appetit" : charge - annacharge)
