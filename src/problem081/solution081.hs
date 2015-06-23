import Data.Text (pack, unpack, splitOn)

main = do
    content <- readFile "matrix.txt"
    let matrix = [map (\n ->  read n :: Int) . split "," $ line | line <- lines content]
    print . minimum . foldl1 diagSum . diags $ matrix

diagSum :: [Int] -> [Int] -> [Int]
diagSum xs@(x0:xs') ys = map (\(a, b, c) -> a + min b c) $ zip3 ys xs0 xs1
    where xs0 = xs ++ [head $ reverse xs]
          xs1 = if length xs < length ys then x0:xs else xs'

diags :: [[Int]] -> [[Int]]
diags matrix = map diagByIdx $ [0..diagMax]
    where xMax = (length matrix) - 1
          yMax = (length $ matrix !! 0) - 1
          diagMax = xMax + yMax
          diagByIdx d = [
            matrix !! x !! y | x <- [0..(min d xMax)], y <- [0..(min d yMax)], x + y == d]

split :: String -> String -> [String]
split delimiter = map unpack . splitOn (pack delimiter) . pack
