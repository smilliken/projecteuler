import Data.List (permutations, sort)
main = print . (!! 999999) . sort . permutations $ "0123456789"
