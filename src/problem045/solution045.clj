(defn is-pentagonal[n]
    (def k (/ (+ (Math/sqrt (+ (* 24 n) 1)) 1) 6))
    (= (- k (int k)) 0.0))

(defn is-hexagonal[n]
    (def k (/ (+ (Math/sqrt (+ (* 8 n) 1)) 1) 4))
    (= (- k (int k)) 0.0))

(println
    (first
        (drop-while #(or (not (is-pentagonal %)) (not (is-hexagonal %)) (< % 40756))
            (map #(/ (* % (+ % 1)) 2)
                (iterate inc 1)))))
