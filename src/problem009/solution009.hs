main = print . head . map (\(a, b, c) -> a * b * c) . filter isPythagorean $
       [(a, b, 1000 - a - b) | a <- [1..1000], b<-[1..(1000 - 1 - a)]]
isPythagorean (a, b, c) = a^2 + b^2 == c^2