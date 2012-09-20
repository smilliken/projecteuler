object Euler142 {
    def main(args: Array[String]) {
        var a = 0
        while (true) {
            a += 1
            for (c <- 1 until a) {
                if (perfectsq(math.sqrt(math.pow(a, 2) - math.pow(c, 2)))) {
                    for (b <- 1 until a) {
                        var x = ((math.pow(a, 2) + math.pow(b, 2)) / 2).toInt
                        var y = ((math.pow(a, 2) - math.pow(b, 2)) / 2).toInt
                        var z = (x - math.pow(c, 2)).toInt
                        if (y > z && z > 0
                            && perfectsq(math.sqrt(x + z))
                            && perfectsq(math.sqrt(x - z))
                            && perfectsq(math.sqrt(y + z))
                            && perfectsq(math.sqrt(y - z))) {
                            println(x + y + z)
                            return
                        }
                    }
                }
            }
        }
    }

    def perfectsq(n: Double): Boolean = {
        return n == n.toInt
    }
}