import Data.Set (fromList, toList, difference)

ceil = 28123
main = print . sum . toList $ difference (fromList [1..ceil]) abundantSums
abundantSums = fromList $ [x + y | x <- abundantNums, y <- abundantNums, x + y <= ceil]
abundantNums = filter isAbundant $ [1..ceil]
isAbundant n = n < (sum . filter (\d -> n `mod` d == 0) $ [1..(n `div` 2)])
