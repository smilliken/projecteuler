main = print . sum . filter isCurious $ [3..10^5]
isCurious n = n == (sum . map (\d -> product [1..d]) . digits $ n)
digits n = map (\d -> read [d]::Int) . show $ n
