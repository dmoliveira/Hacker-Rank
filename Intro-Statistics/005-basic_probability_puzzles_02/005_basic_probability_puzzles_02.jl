#!/usr/bin/env julia
total_sum = 6
all_2dices_toss = [
    t1+t2 == total_sum && t1 != t2? 1 : 0
    for t1=1:6, t2=1:6
]
all_tosses = length(all_2dices_toss)
event_tosses = sum(all_2dices_toss)
println("The probability is: $(event_tosses//all_tosses)")

