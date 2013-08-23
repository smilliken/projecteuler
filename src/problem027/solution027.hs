import Data.List (takeWhile)
main = print $ a * b
    where (l, a, b) = maximum
            . map (\(a, b) -> (runLength isPrime (quadraticSeries a b), a, b))
            $ [(a, b) | a<-[-999..999], b<-[-999..999]]
quadraticSeries a b = map (\n -> n^2 + a * n + b) $ [0..]
runLength p l = length . takeWhile p $ l
isPrime n = elem n . takeWhile (<=n) $ primes
primes = 2 : [x | x <- [3..],
    all (\p -> x `mod` p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]
