import Data.Char (isDigit)
import Data.List (tails)

main = do
    content <- readFile "number.txt"
    let digits = map (\x -> read[x]::Int) . filter isDigit $ content
    print . maximum . map (product . take 5) . tails $ digits
