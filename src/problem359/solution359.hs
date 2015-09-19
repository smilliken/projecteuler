main = print $ n `mod` (10 ^ 9)
    where n = sum [occupant f r | e2 <- [0..27], e3 <- [0..12],
                                  let f = 2 ^ e2 * 3 ^ e3, let r = 2 ^ (27 - e2) * 3 ^ (12 - e3)]

-- | summation of squares 1 to n with alternating sign
altSquares n = n * (n + 1) `div` 2

-- | occupant number at floor f, room r
occupant 1 1 = 1
occupant f 1 = f ^ 2 `div` 2
occupant f r = altSquares (r2rt + r - 2) + sign * (altSquares (r2rt - 1) - occupant f 1)
    where sign = if even r then 1 else -1
          r2rt = if f == 1 then 2 else if even f then f + 1 else f
