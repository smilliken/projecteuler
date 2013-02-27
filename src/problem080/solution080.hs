import Data.List

main = print . sum $ [sqrtSum x | x <- [1..100] \\ (map (^2) [1..10])]
sqrtSum n = sum . map (\x -> read [x]::Integer) . show $ jarvisSqrt n 100
--http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
jarvisSqrt n precision = (jarvisSqrtRecur (5 * n) 5 (precision + 2)) `div` 100
jarvisSqrtRecur a b precision
	| (length $ show b) >= precision = b
	| a >= b = jarvisSqrtRecur (a - b) (b + 10) precision
	| otherwise = jarvisSqrtRecur (a * 100) ((b `div` 10) * 100 + 5) precision
