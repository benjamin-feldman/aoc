(ns day1
  (:require [clojure.string]))

(defn get-split-lines [filepath]
  (let [lines (clojure.string/split-lines (slurp filepath))]
    (reduce
     (fn [[lefts rights] line]
       (let [[left right] (clojure.string/split line #"\s{3,}")]
         [(conj lefts left)
          (conj rights right)]))
     [[] []]
     lines)))

;; Part 1

(defn first-part [filepath]
  (let [[left-nums right-nums] (get-split-lines filepath)
        sorted-left (sort left-nums)
        sorted-right (sort right-nums)
        differences (map #(Math/abs (- (parse-long %1)
                                       (parse-long %2)))
                         sorted-left
                         sorted-right)]
    (reduce + differences)))

;; Part 2

(defn counter-hashmap [coll]
  (reduce (fn [counts item]
            (update counts item (fnil inc 0)))
          {}
          coll))

(defn second-part [filepath]
(  let [
        [left-nums right-nums] (get-split-lines filepath) 
        right-counter (counter-hashmap right-nums)

        similarities (map #(* (parse-long %) (right-counter % 0)) left-nums)
        ]
 (reduce + similarities)
 ))


