import List
main = putStrLn $ show $ head $ filter check [1..]
digits x = sort $ map(\z -> read [z]::Int) (show $ x)
check x = digits (x * 2) == digits (x * 3) && digits (x * 2) == digits (x * 4) && digits (x * 2) == digits (x * 5) && digits (x * 2) == digits (x * 6)