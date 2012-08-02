(def target 2000000)
(defn dist[n m]
  (def squares (/ (* n (inc n) m (inc m)) 4))
  (if (> squares target) (- squares target) (- target squares)))
(defn winner[x y]
  (if (< (first x) (first y)) x y))
(println (last (reduce winner
    (for [x (range 200) y (range 200)]
      [(dist x y) x y (* x y)]))))
