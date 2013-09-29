main = do
    content <- readFile "numbers.txt"
    let numbers = map (\line -> read line :: Integer) . words $ content
    print . (\x -> read x :: Integer) . take 10 . show . sum $ numbers
