import Data.List (takeWhile, foldl1')

main = print . snd . foldl1' max . map (\(a, b) -> (quadPrimes a b, a * b)) $
       [(a, b) | a<-[-999..999], b<-[-999..999]]
quadPrimes a b = length . takeWhile isPrime . map (\n -> n^2 + a * n + b) $ [0..]
isPrime n = elem n . takeWhile (<=n) $ primes
primes = 2 : [x | x <- [3..],
    all (\p -> x `mod` p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]
