#!/usr/bin/env scala
object Solution {
    def main(args: Array[String]) {
        var n = readLine
        var numbers = readLine.split(" ").map(_.toInt).sorted
        var mean = numbers.sum.toFloat/numbers.length
        var median_index = numbers.length/2
        var median = if(numbers.length % 2 != 0) {
                        numbers(median_index)
                    } else {
                        (numbers(median_index)+numbers(median_index-1))/2.toFloat
                    }
        var group = numbers.groupBy(i => i).mapValues(_.size)
        var max_value = 0
        var group_value = Int.MaxValue
        for((group, value) <- group if value >= max_value && group <= group_value) {max_value = value; group_value = group}
        var mode = group_value 
        var std = math.sqrt(numbers.map(_ - mean).map(math.pow(_, 2)).sum/numbers.length)
        printf("%.1f\n", mean)
        printf("%.1f\n", median)
        println(mode)
        printf("%.1f", std)
    }
}
