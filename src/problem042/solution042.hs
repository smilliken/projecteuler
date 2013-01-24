import Data.Char (ord)
import Data.Text (pack, unpack, replace, splitOn)

main = do
    raw <- readFile "words.txt"
    print . length . filter isTriangle . map digitsum . map unpack . map (replace (pack "\"") (pack "")) . splitOn (pack ",") $ pack raw
digitsum = sum . map (\x -> (ord x) - 64)
isTriangle n = ceiling idx == floor idx where idx = (sqrt (1 + 8 * (fromIntegral n)) - 1) / 2