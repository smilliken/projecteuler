main = print . maximum . pfactors $ 600851475143
pfactors 1 = []
pfactors n = pfactor n : pfactors (div n (pfactor n))
pfactor n = head . filter (\x -> mod n x == 0) $ [2..n]