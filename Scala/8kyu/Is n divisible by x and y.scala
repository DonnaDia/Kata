object Kata {
  def isDivisible(n: Int, x: Int, y: Int): Boolean = {
  if (n % x == 0 && n % y == 0) true else false
  }
}