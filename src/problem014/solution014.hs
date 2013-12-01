import Data.Word (Word32)
import Data.List (foldl1')
import Data.Ord (comparing)

collatzOdd :: Word32 -> [Word32]
collatzOdd 1 = [1]
collatzOdd n = n : collatzOdd ((if even n then n else 3 * n + 1) `div` 2)
maximumBy' cmp = foldl1' (\a b -> case cmp a b of GT ->  a; _ -> b)
main = print . head . maximumBy' (comparing length) . map collatzOdd $ [1..1000000]
