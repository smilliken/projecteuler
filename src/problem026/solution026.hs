main = print $ d
    where (len, d) = maximum . map (\d -> (fracPeriod d, d)) $ [2..999]
fracPeriod d =
    head [i2 - i1 | (i1, r1) <- divr d, (i2, r2) <- take d . drop i1 $ divr d, i1 < i2, r1 == r2]
divr d = zip [1..] (divr' 1 d)
divr' n d = let r = n * 10 `mod` d in r : divr' r d
