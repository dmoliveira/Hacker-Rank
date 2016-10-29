#!/usr/bin/env julia
maxsum = 9
vector = [i+j for i=1:6, j=1:6]
sums_number = length(vector[vector .<= maxsum])
numbers = length(vector)
println(
    string(
        "Number of sums of two dices ⩽ $maxsum: ",
        "$(sums_number//numbers)"
    )
)
