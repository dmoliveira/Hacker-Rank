# There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location  and moves at a rate of  meters per jump. The second kangaroo starts at location  and moves at a rate of  meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?
# https://www.hackerrank.com/challenges/kangaroo/problem
x1, v1, x2, v2 = map(x->parse(Int, x), split(readstring(STDIN)))
ans = (v1==v2 && x1==x2) || (x1 < x2 && v1 > v2 && (x1-x2) % (v1-v2) == 0) ? "YES" : "NO"
println(ans)
