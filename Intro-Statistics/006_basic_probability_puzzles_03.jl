#!/usr/bin/env julia
probabilities = (
    (4//7 * 5//9 * 4//8) + # RRB
    (4//7 * 4//9 * 4//8) + # RBR
    (3//7 * 5//9 * 4//8)   # BRR
)
println("Probability: $probabilities")
