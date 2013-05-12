import Text.Printf (printf)
main = printf "%d\n" $ combinations 40 20
combinations n k = ((product [1..n]) `div` (product [1..k] * product [1..(n - k)]))::Integer