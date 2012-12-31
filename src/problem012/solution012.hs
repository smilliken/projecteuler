trianglenum n = div (n * (n + 1)) 2
divisors n = 1 + length [d | d <- [1..(div n 2)], mod n d == 0]
triangledivisors n = if mod n 2 == 0 then (divisors (div n 2)) * (divisors (n + 1)) else (divisors n) * (divisors (div (n + 1) 2))
main = print . head . filter (\(n, d) -> d > 500) . map (\n -> (trianglenum n, triangledivisors n)) $ [1..]