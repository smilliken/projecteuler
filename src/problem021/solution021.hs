main = print . sum . filter isAmicable $ [2..9999]
isAmicable a = a == d b && a /= b where b = d a
d n = sum . filter (\i -> n `mod` i == 0) $ [1..(n `div` 2)]
