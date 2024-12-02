(ns aoc2024.day1
  (:require [clojure.string :as str]))

(defn calculate-difference []
  (let [
        lines (str/split-lines (slurp "resources/day1/input.txt"))
        
        [left-nums right-nums] 
        (reduce 
          (fn [[lefts rights] line]
            (let [[left right] (str/split line #"\s{3,}")]
              [(conj lefts left) 
               (conj rights right)]))
          [[] []]
          lines)
        
        sorted-left (sort left-nums)
        sorted-right (sort right-nums)
        
        differences (map #(Math/abs (- (parse-long %1) 
                                     (parse-long %2))) 
                        sorted-left 
                        sorted-right)]
    
    (reduce + differences)))

(defn -main [& args]
  (println (calculate-difference)))