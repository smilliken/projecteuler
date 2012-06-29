import List
main = putStrLn $ show $ fst $ bouncyrecur 0 0
digits x = map(\z -> read [z]::Int) (show $ x)
isbouncy x = digits x /= (sort $ digits x) && digits x /= (reverse $ sort $ digits x)
bouncyrecur n bouncy_count = if (n > 1 && div (bouncy_count * 100) (n - 1) == 99) then (n - 1, bouncy_count) else bouncyrecur (n + 1) (bouncy_count + (if isbouncy(n) then 1 else 0))