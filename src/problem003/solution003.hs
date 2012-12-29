main = print . maximum . pfactors $ 600851475143
pfactors 1 = []
pfactors n = do
    let pn = pfactor n
    return pn ++ pfactors (div n pn)
pfactor n = head . filter (\x -> mod n x == 0) $ [2..n]