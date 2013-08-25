main = print . sum . filter check . map pwrSum . drop 2 $ digits 7 9
check n = n == (pwrSum . map (\d -> read [d]::Int) $ show n)
pwrSum = sum . map (^5)
digits 0 ceil = [[]]
digits n ceil = [i : rest | i<-[0..ceil], rest<-digits (n - 1) i]
