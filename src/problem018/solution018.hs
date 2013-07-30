import Data.List (zipWith)

main = do
    content <- readFile "triangle.txt"
    let rows = map (\line -> [read x::Int | x <- words line]) $ lines content
    print . head . foldr1 (\r1 r2 -> zipWith (+) r1 (reduce r2)) $ rows

reduce row = zipWith max row (tail row)
