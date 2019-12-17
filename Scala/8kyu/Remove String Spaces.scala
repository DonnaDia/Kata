//Vers 1
object Kata {

  def noSpace(s: String): String = s.replaceAll("\\s", "")
}

//Vers 2
object Kata {

  def noSpace(s: String): String = {
    s.replace(" ", "")
  }
}

//Vers 3
object Kata {

  def noSpace(s: String): String = {
    s.replaceAll(" ", "")
  }
}