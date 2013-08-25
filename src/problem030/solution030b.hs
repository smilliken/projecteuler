main = print . sum . filter check $ [2..10^7]
check n = n == (sum . map (^5) . map (\d -> read [d]::Int) $ show n)
