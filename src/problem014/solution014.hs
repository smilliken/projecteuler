-- Must run with optimizations! (-O2 flag in GHC)
import Data.List (maximumBy)
collatz 1 = [1]
collatz n = n : collatz (if even n then n `div` 2 else 3 * n + 1)
main = print . fst . maximumBy (\(_, nlen) (_, mlen) -> compare nlen mlen) . map (\n -> (n, length . collatz $ n)) $ [1..1000000]