package main

import "fmt"

func main() {
    count := 0
    for d := 1; d <= 12000; d++ {
        for n := d / 3 + 1; n * 2 < d; n++ {
            if gcd(d, n) == 1 {
                count++
            }
        }
    }
    fmt.Println(count)
}

func gcd(a, b int) int {
    if b == 0 {
        return a
    }
    return gcd(b, a % b)
}