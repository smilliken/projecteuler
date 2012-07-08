package main

import "fmt"
import "strconv"

func main() {
    limit := uint64(100000000)
    square_sums := []uint64{}
    for i := uint64(0); i < limit; i++ {
        square_sums = append(square_sums, (uint64)(i * (i + 1) * (2 * i + 1) / 6))
        if i * i > limit {
            break
        }
    }
    palins := []uint64{}
    for i := 0; i < len(square_sums); i++ {
        for j := 0; j < i; j++ {
            sq_sum := square_sums[i] - square_sums[j]
            if i - j > 1 && sq_sum < limit && strconv.Uitoa64(sq_sum) == Reverse(strconv.Uitoa64(sq_sum)) {
                exists := false
                for k := 0; k < len(palins); k++ {
                    if palins[k] == sq_sum {
                        exists = true
                    }
                }
                if !exists {
                    palins = append(palins, sq_sum)
                }
            }
        }
    }
    sum := uint64(0)
    for _, palin := range palins {
        sum += palin
    }
    fmt.Println(sum)
}

func Reverse(s string) (result string) {
  for _, v := range s {
    result = string(v) + result
  }
  return 
}