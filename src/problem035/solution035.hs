import Data.Set (fromList, member, toList)
main = print . length . filter isCircular . toList $ primes
isCircular p = all (\x -> x `member` primes) $ [take len . drop x $ cycle p | x <- [1..(len - 1)]]
    where len = length p
primeGen = 2 : [x | x <- [3..], all (\p -> mod x p /= 0) . takeWhile (\p -> p^2 <= x) $ primeGen]
primes = fromList . map show . takeWhile (<=1000000) $ primeGen
