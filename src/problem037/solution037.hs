main = print . sum . take 11 . filter truncatable $ primes
primes = 2 : [x | x <- [3..],
              all (\p -> x `mod` p /= 0) . takeWhile (\p -> p^2 <= x) $ primes]
isPrime n = elem n . takeWhile (<=n) $ primes
truncatable p = (rightTruncatable p) && (leftTruncatable p)
rightTruncatable p = isPrime p' && (p' < 10 || rightTruncatable p')
  where p' = p `div` 10
leftTruncatable p = isPrime p' && (p' < 10 || leftTruncatable p')
  where p' = p `mod` (10 ^ (floor $ logBase 10 (fromIntegral p :: Float)))
