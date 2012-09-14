object Euler188 {
    def main(args: Array[String]) {
        var residue = BigInt(1)
        for (idx <- 1 until 1855) {
            residue = BigInt(1777).modPow(residue, 100000000)
        }
        println(residue)
    }
}