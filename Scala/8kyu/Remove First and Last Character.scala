object RemoveFirstAndLastCharacters {
  def removeChars(s: String): String = {
    s.drop(1).dropRight(1)
  }
}