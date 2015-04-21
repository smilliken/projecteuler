import Data.Text (pack, unpack, splitOn)

main = do
    content <- readFile "matrix.txt"
    let matrix = [map (\n ->  read n :: Int) . split "," $ line | line <- lines content]
    print . head . foldl1 diagSum . diags $ matrix

enum :: [a] -> [(Int, a)]
enum xs = zip [1..] xs

diagSum :: [Int] -> [Int] -> [Int]
diagSum xs ys = map cellSum $ enum ys
    where xMax = length xs
          yMax = length ys
          neighbor xIdx yIdx = xIdx == yIdx || (yIdx - xIdx) == (if xMax < yMax then 1 else -1)
          cellSum (yIdx, y) = minimum [x + y | (xIdx, x) <- enum xs, neighbor xIdx yIdx]

diags :: [[Int]] -> [[Int]]
diags matrix = map diagByIdx $ [0..diagMax]
    where xMax = (length matrix) - 1
          yMax = (length $ matrix !! 0) - 1
          diagMax = xMax + yMax
          diagByIdx d = [
            matrix !! x !! y | x <- [0..(min d xMax)], y <- [0..(min d yMax)], x + y == d]

split :: String -> String -> [String]
split delimiter = map unpack . splitOn (pack delimiter) . pack
