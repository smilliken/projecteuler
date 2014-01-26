main = print . product . map getDigit $ [10 ^ x | x <- [0..6]]
getDigit n = read [digits !! (n - 1)] :: Int
digits = concat . map show $ [1..]
