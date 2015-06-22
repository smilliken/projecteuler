main = do
    content <- readFile "triangle.txt"
    let rows = [map (\n ->  read n :: Int) . words $ line | line <- lines content]
    print . maximum . foldl1 rowsum $ rows

rowsum :: [Int] -> [Int] -> [Int]
rowsum r0 r1 = map (\(a, b, c) -> a + max b c) $ zip3 r1 (0:r0) (r0 ++ [0])
