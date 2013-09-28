import Data.List (foldl1')
import Data.Ord (comparing)

collatz 1 = [1]
collatz n = n : collatz (if even n then n `div` 2 else 3 * n + 1)
maximumBy' cmp = foldl1' (\a b -> case cmp a b of GT ->  a; _ -> b)
main = print . head . maximumBy' (comparing length) . map collatz $ [1..1000000]
