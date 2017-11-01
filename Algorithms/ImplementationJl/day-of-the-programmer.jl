# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
numbers()::Vector{Int} = map(n->parse(Int,n), split(readline(STDIN), " "))

DayOfProgrammer = 256
YearChange = 1918

year = numbers()[1]
date = Date(year, 1, 1) + Dates.Day(DayOfProgrammer-1) + Dates.Day(year != YearChange? 0 : 13)
if year < YearChange
    date += !Dates.isleapyear(year) && year % 4 == 0? Dates.Day(-1) : Dates.Day(0)
end
println(Dates.day(date), ".0", Dates.month(date), ".", Dates.year(date))
