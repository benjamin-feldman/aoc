(ns day2
  (:require [clojure.string :as str]))

(defn get-split-lines [filepath]
  (map (fn [line] (map #(Long/parseLong %) (str/split line #"\s+")))
       (str/split-lines (slurp filepath))))

;; Part 1

(defn safe [coll]
  (let [deltas (map (fn [[a b]] (- b a)) (partition 2 1 coll))]
    (and (every? #(<= 1 (Math/abs %) 3) deltas)
         (or (every? pos? deltas)
             (every? neg? deltas)))))

(defn first-part [filepath]
  (let [lines (get-split-lines filepath)]
    (count (filter safe lines))))

;; Part 2

(defn coll-except-one [coll]
  (map (fn [idx] (concat (take idx coll) (drop (inc idx) coll))) (range (count coll))))


(defn safe-dampener [coll]
  (or (safe coll)
      (reduce #(or %1 %2) false (map safe (coll-except-one coll)))))

(defn second-part [filepath]
  (let [lines (get-split-lines filepath)]
    (count (filter safe-dampener lines))))