main = print . sum . map (\a -> a^2 - (if odd a then a else 2 * a)) $ [3..1000]
