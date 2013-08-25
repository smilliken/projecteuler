main = print . length $ combinations 200 [1, 2, 5, 10, 20, 50, 100, 200]
combinations n [] = [[]]
combinations n coins = [i : rest | let c = head coins, i<-[0..(n `div` c)],
    rest<-combinations (n - i * c) (tail coins), n == (total (i : rest) coins)]
total counts coins = sum . map (\(c, n) -> c * n) $ zip counts coins
