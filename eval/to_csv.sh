#!/usr/bin/env bash

echo 'type,ngram,method,cutoff,f1,precision,recall' > results.csv
cat results.txt | tr '\n' ',' | sed 's/,,/\n/g' | sed 's/F1 score: //g' | sed 's/Precision: //g' | sed 's/Recall: //g' | sed 's/ /,/g' >> results.csv