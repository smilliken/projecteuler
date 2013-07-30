import Data.Char (isAlpha)

main = print . length . filter isAlpha .
    foldl (\x y -> x ++ "\n" ++ y) "\n" . map toEnglish $ [1..1000]

toEnglish n
    | n >= 1000 = names (n `div` 1000) ++ " " ++ names 1000 ++ " " ++
        toEnglish (n `mod` 1000)
    | n >= 100 && (n `mod` 100 > 0) = names (n `div` 100) ++ " " ++
        names 100 ++ " and " ++ toEnglish (n `mod` 100)
    | n >= 100 = names (n `div` 100) ++ " " ++ names 100 ++ " " ++
        toEnglish (n `mod` 100)
    | n >= 20 && n `mod` 10 > 0 = names ((n `div` 10) * 10) ++ "-" ++
        toEnglish (n `mod` 10)
    | n >= 20 = names ((n `div` 10) * 10) ++ " " ++
        toEnglish (n `mod` 10)
    | n >= 1 = names n
    | n == 0 = ""

names n
    | n == 1 = "one" | n == 2 = "two" | n == 3 = "three" | n == 4 = "four"
    | n == 5 = "five" | n == 6 = "six" | n == 7 = "seven" | n == 8 = "eight"
    | n == 9 = "nine" | n == 10 = "ten" | n == 11 = "eleven"
    | n == 12 = "twelve" | n == 13 = "thirteen" | n == 14 = "fourteen"
    | n == 15 = "fifteen" | n == 16 = "sixteen" | n == 17 = "seventeen"
    | n == 18 = "eighteen" | n == 19 = "nineteen" | n == 20 = "twenty"
    | n == 30 = "thirty" | n == 40 = "forty" | n == 50 = "fifty"
    | n == 60 = "sixty" | n == 70 = "seventy" | n == 80 = "eighty"
    | n == 90 = "ninety" | n == 100 = "hundred" | n == 1000 = "thousand"
