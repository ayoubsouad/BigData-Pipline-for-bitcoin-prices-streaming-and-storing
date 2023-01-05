package sample

object Main {
  def main(args: Array[String]) = {
    println("START")
    //kafka
    val kafka = new Consumer()
    kafka.loadKafka("binance-topic")
    kafka.writeData()
    println("Done")

  }
}
