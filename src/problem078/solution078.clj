(defn pentagonal[n]
  (/ (* n (- (* 3 n) 1)) 2))
(def partitions
  (memoize
    (fn [n]
      (if (<= n 1) 1
          (reduce +' 
            (map #(* (if (= (mod (first %) 2) 1) 1 -1) (partitions (- n (second %))))
              (take-while #(<= (second %) n)
                (map (fn [i] [i (pentagonal i)]) 
                  (map #(- 0 (quot (* % (if (= (mod % 2) 1) 1 -1)) 2))
                    (iterate inc 2))))))))))
(println
  (first
    (first (drop-while (fn [tup] (> (mod (second tup) 1000000) 0))
      (map (fn [n] [n (partitions n)])
        (iterate inc 1))))))
