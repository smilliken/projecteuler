import Data.List (zipWith)
main = print $ n
     where (n, fib) = head . filter (\(n, fib) -> fib >= 10 ^ 999) . zip [1..] $ fibs
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

