object SumOfPositive {
  def positiveSum(arr: Array[Int]): Int = {
    var result = 0
    for (el <- arr if el > 0) result += el
    result
  }
}