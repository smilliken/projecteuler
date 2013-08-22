main = print $ d
    where (len, d) = maximum . map (\d -> (fractionPeriod d, d)) $ [2..999]
fractionPeriod d = head [i2 - i1 |
    (i1, r1) <- divr d, (i2, r2) <- take d . drop i1 $ divr d,
    i1 < i2, r1 == r2]
divr d = zip [1..] (divr' 1 d)
divr' n d = (res, rem) : divr' rem d
    where n' = n * 10
          res = n' `div` d
          rem = n' `mod` d

