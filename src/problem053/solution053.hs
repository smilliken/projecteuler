main = print . length . filter (>=1000000) $ [n `choose` k | n <- [1..100], k <- [0..n]]
n `choose` k = factorial n `div` ((factorial k) * (factorial (n - k)))
factorial n = product [1..n]
