#!/usr/bin/env scala
object Solution {
  def main(args: Array[String]) {
   val value = 0.9025
   val mean = 0.675
   val std = 0.065
   val z = zscore(value, mean, std) 
   printf("z-score: %.2f", z)
  } 
  def zscore(value: Double, mean: Double, std: Double) = (value-mean)/std
}
