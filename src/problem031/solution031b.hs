main = print . show . (+1) . length $ [1 | p1 <- [0..200], p2 <- [0..100],
    p5 <- [0..40], p10 <- [0..20], p20 <- [0..10], p50 <- [0..4],
    p100 <- [0..2], (p1 * 1 + p2 * 2 + p5 * 5 + p10 * 10 + p20 * 20 +
        p50 * 50 + p100 * 100) == 200]
