import Data.List (sort)

main = print . maximum . filter check $
       [concatProd n x | n <- [2..9], x <- [1..10 ^ (9 `div` n)]]
concatProd :: Int -> Int -> String
concatProd n x = concat . map show $ [x * i | i <- [1..n]]
check :: String -> Bool
check x = (sort $ x) == "123456789"
