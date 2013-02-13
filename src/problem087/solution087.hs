import Data.List
main = print . length . group . sort $ [a | c <- powersum 2 0, b <- powersum 3 c, a <- powersum 4 b]
powersum pow running = takeWhile (<50000000) $ map (\x -> x ^ pow + running) $ primes
primes = 2 : [x | x <- [3..], all (\p -> x `mod` p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]