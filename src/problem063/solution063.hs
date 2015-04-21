main = print . length $ [(base, pow) | base <- [1..9], pow <- [1..22], check base pow]
check :: Int -> Int -> Bool
check base pow = pow == (length . show $ base ^ pow)
