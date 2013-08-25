main = print . sum . diagonals $ [1..(1001^2)]
diagonals = diagonals' 2
diagonals' n [] = []
diagonals' n l = take 4 (everyBy n l) ++ diagonals' (n + 2) (drop (4 * n) l)
everyBy n [] = []
everyBy n l = head l : (everyBy n $ drop n l)
