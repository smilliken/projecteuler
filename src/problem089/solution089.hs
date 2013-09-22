main = do
    numerals <- readFile "roman.txt"
    print . sum . map diffline . lines $ numerals
diffline numeral = (length numeral) - (length . toRoman . fromRoman $ numeral)
fromRoman "" = 0
fromRoman [c] = fromRomanChr c
fromRoman n = fromRoman(tail n) + (if d1 < d2 then -d1 else d1)
    where (d1:d2:rest) = map fromRomanChr $ n
fromRomanChr c
    | c == 'I' = 1 | c == 'V' = 5 | c == 'X' = 10 | c == 'L' = 50 | c == 'C' = 100
    | c == 'D' = 500 | c == 'M' = 1000 | otherwise = 0
toRoman n
    | n >= 1000 = "M" ++ toRoman (n - 1000)
    | n >= 900 = "CM" ++ toRoman (n - 900)
    | n >= 500 = "D" ++ toRoman (n - 500)
    | n >= 400 = "CD" ++ toRoman (n - 400)
    | n >= 100 = "C" ++ toRoman (n - 100)
    | n >= 90 = "XC" ++ toRoman (n - 90)
    | n >= 50 = "L" ++ toRoman (n - 50)
    | n >= 40 = "XL" ++ toRoman (n - 40)
    | n >= 10 = "X" ++ toRoman (n - 10)
    | n >= 9 = "IX" ++ toRoman (n - 9)
    | n >= 5 = "V" ++ toRoman (n - 5)
    | n >= 4 = "IV" ++ toRoman (n - 4)
    | n >= 1 = "I" ++ toRoman (n - 1)
    | otherwise = ""
