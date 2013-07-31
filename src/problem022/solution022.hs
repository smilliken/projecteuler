import Data.Char (ord)
import Data.List (dropWhileEnd, sort, zipWith)

main = do
    content <- readFile "names.txt"
    print . sum . zipWith score [1..] . sort .
        map (strip '"') . split ',' $ content

score idx = (*idx) . (sum . map ((+(1-ord 'A')) . ord))

split chr "" = []
split chr str = part : (split chr $ dropWhile (==chr) rest)
    where (part, rest) = break (==chr) str

strip chr = dropWhileEnd (==chr) . dropWhile (==chr)
