import Data.List (permutations, tails)

main = print . sum . map read . filter valid . permutations $ "0123456789"

valid :: String -> Bool
valid ('0':_) = False
valid (_:s) = all (\(d, n) -> n `mod` d == 0) $ divs
    where divs = reverse . zip [2, 3, 5, 7, 11, 13, 17] $ groups
          groups = map (read . take 3) . tails $ s
