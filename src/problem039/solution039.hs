import Data.List (group, maximumBy, sort)
import Data.Function (on)
maxPerim = 1000
main = print . fst . maximumBy (compare `on` snd) . map (\xs -> (head xs, length xs)) . group . sort $ solns
    where solns = [truncate (x + y + z) | x <- [1..maxPerim], y <- [1..(maxPerim-x)], let z = sqrt(x ^ 2 + y ^ 2), x + y + z <= maxPerim, floor z == ceiling z]