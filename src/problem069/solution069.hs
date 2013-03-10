main = print . last . takeWhile (<=1000000) $ scanl1 (*) primes
primes = 2 : [x | x <- [3..], all (\p -> x `mod` p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]
