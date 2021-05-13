#!/usr/bin/env bash

# model type ['w', 'w_and_c', 'w_plus_c']
# n-gram order
# method ['witten_bell', 'absolute', 'katz', 'kneser_ney', 'presmoothed', 'unsmoothed']
# cutoff

for mtype in 'w' 'w_and_c' 'w_plus_c'
do
    for ngram in {1..5}
    do
        for method in 'witten_bell' 'absolute' 'katz' 'kneser_ney' 'presmoothed' 'unsmoothed'
        do
            for cutoff in 0 2
            do
                (cd ../src; echo $mtype $ngram $method $cutoff && python3 main.py $mtype $ngram $method $cutoff && printf "\n")
            done
        done
    done
done > results.txt