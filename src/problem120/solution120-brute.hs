main = print . sum . map maxpolyrem $ [3..1000]

maxpolyrem :: Integer -> Integer
maxpolyrem a = maximum . map (polyrem a) $ [1..(2 * a)]

polyrem :: Integer -> Integer -> Integer
polyrem a n = ((a - 1) ^ n + (a + 1) ^ n) `mod` (a ^ 2)
