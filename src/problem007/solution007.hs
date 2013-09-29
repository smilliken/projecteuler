main = print . head . drop 10000 $ primes
primes = 2 : [x | x <- [3..],
    all (\p -> mod x p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]