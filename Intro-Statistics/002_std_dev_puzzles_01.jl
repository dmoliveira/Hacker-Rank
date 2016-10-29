#!/usr/bin/env julia
σ1 = round(std([1,2,3]), 2)
for n=0:.01:100000
    σ = round(std([1,2,3,n]),2)
    σ == σ1 && (println("$n"))
end
