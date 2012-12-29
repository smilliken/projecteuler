main = print . sum . filter (\x -> mod x 2 == 0) . takeWhile (\x -> x <= 4000000) . map fib $ [1..]
fib 1 = 1
fib 2 = 2
fib x = fib (x - 1) + fib (x - 2)