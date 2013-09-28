import Data.List (group, maximumBy, sort)
import Data.Function (on)

main = print . head . maximumBy (compare `on` length) . group . sort $ solns
    where solns = let perim = 1000 in [truncate (x + y + z) |
            x <- [1..perim], y <- [1..(perim - x)], let z = sqrt(x ^ 2 + y ^ 2),
            x + y + z <= perim, floor z == ceiling z]