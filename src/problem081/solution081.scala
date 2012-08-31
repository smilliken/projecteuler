object Euler081 {
    def main(args: Array[String]) {
        val lines = scala.io.Source.fromFile("matrix.txt").getLines
        var matrix = lines.map(n => n.split(',').map(m => Integer.parseInt(m))).toArray
        for (pathlen <- 1 until 159) {
            for (col <- List(pathlen - 79, 0).max until List(pathlen + 1, 80).min) {
                var sumcandidates = List[Int]()
                if (pathlen - col == 0) {
                    sumcandidates = sumcandidates ::: List(matrix(0)(col - 1))
                }
                else if (col == 0) {
                    sumcandidates = sumcandidates ::: List(matrix(pathlen - 1)(0))
                }
                else {
                    sumcandidates = sumcandidates ::: List(matrix(pathlen - col)(col - 1))
                    sumcandidates = sumcandidates ::: List(matrix(pathlen - col - 1)(col))
                }
                matrix(pathlen - col)(col) = matrix(pathlen - col)(col) + sumcandidates.min
            }
        }
        println(matrix(79)(79))
    }
}