width = 20
height = 20
cell nums x y = nums !! (y * width + x)
diagonal nums (x, y) (xdir, ydir) =
    product $ [cell nums (x + i * xdir) (y + i * ydir) |
               i <- [0..3], x + i * xdir < width, x + i * xdir >= 0,
               y + i * ydir < height, y + i * ydir >= 0]
main = do
    content <- readFile "grid.txt"
    let nums = map (\x -> read x::Int) . words $ content
    print . maximum $ [diagonal nums (x, y) dir |
                       x <- [0..(width-1)], y <- [0..(height-1)],
                       dir <- [(1, -1), (1, 0), (1, 1), (0, 1)]]
