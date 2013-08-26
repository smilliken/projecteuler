import Data.List (group, sort, permutations, zipWith)
main = print . sum . map head . group . sort $ [z | digits<-permutations [1..9],
    mulIdx<-[1..7], eqIdx<-[(mulIdx + 1)..8],
    let x = toInt . take mulIdx $ digits,
    let y = toInt . drop mulIdx . take eqIdx $ digits,
    let z = toInt . drop eqIdx $ digits,
    x * y == z]
toInt digits = sum $ zipWith (\d i -> d * 10^i) digits [0..]
