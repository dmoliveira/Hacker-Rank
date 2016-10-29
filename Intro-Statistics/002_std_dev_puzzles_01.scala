#!/usr/bin/env scala
object Solution {
  def main(args: Array[String]) {
    val values1 = Array(1.0,2.0,3.0)
    val std1 = calculateStd(values1)
    printf("Std1: %.2f\n", std1)
    val std2 = findMaxNStd(std1)
    printf("Std2: %.2f", std2)
  }

  def calculateMean(values: Array[Double]) = values.sum/values.length.toFloat
  def calculateStd(values: Array[Double]) = {
    var mean = calculateMean(values)
    var result = values.map(_ - mean).map(math.pow(_, 2)).sum/values.length.toFloat
    math.sqrt(result)
  }
  def findMaxNStd(sigma1: Double) = {
    var sigma1temp = math.BigDecimal(sigma1).setScale(2, BigDecimal.RoundingMode.HALF_UP).toDouble
    var sigma2 = 0.0
    var foundN = false
    var n = .0
    while(n < 100000 && !foundN) {
     var sigma2temp = calculateStd(Array[Double](1.0,2.0,3.0,n)) 
     sigma2temp = math.BigDecimal(sigma2temp).setScale(2, BigDecimal.RoundingMode.HALF_UP).toDouble
     if(sigma2temp == sigma1temp) {
       sigma2 = sigma2temp 
       printf("n:%.2f, std:%.2f\n", n, sigma2temp)
     }
     n += 0.01
    } 
    sigma2
  }
}
