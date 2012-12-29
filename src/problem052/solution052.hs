import Data.List
main = print . head . filter check $ [1..]
digits = sort . map(\z -> read [z]::Int) . show
check x = digits (x * 2) == digits (x * 3) && digits (x * 2) == digits (x * 4) && digits (x * 2) == digits (x * 5) && digits (x * 2) == digits (x * 6)