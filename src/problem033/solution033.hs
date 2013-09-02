import Data.Ratio ((%), denominator)
main = print . denominator . product . map (\(x, y) -> x % y) .
       filter isCurious $ [(x, y) | y<-[10..99], x<-[10..(y - 1)]]
isCurious (x, y) =
  let r = x % y
      (cx, cy) = curiousReduce x y
  in r == (cx % cy) && x > cx
toDigits = map (\c -> read [c]::Int) . show
curiousReduce x y
    | x0 == y1 && y0 > 0 = (x1, y0)
    | x1 == y0 && y1 > 0 = (x0, y1)
    | otherwise = (x, y)
    where (x0:x1:xs) = toDigits x
          (y0:y1:ys) = toDigits y
