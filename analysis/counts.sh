#!/usr/bin/env bash

dpath='../data/NL2SparQL4NLU'

tr_sen=$(cat $dpath.train.utterances.txt | wc -l)
tr_tok=$(cat $dpath.train.conll.txt | sed '/^$/d' | awk '{print $1}' | sort | uniq | wc -l)
tr_tag=$(cat $dpath.train.conll.txt | sed '/^$/d' | awk '{print $2}' | sort | uniq | wc -l)

ts_sen=$(cat $dpath.test.utterances.txt | wc -l)
ts_tok=$(cat $dpath.test.conll.txt | sed '/^$/d' | awk '{print $1}' | sort | uniq | wc -l)
ts_tag=$(cat $dpath.test.conll.txt | sed '/^$/d' | awk '{print $2}' | sort | uniq | wc -l)

j_tok=$(cat $dpath.train.conll.txt $dpath.test.conll.txt | sed '/^$/d' | awk '{print $1}' | sort | uniq | wc -l)
j_tag=$(cat $dpath.train.conll.txt $dpath.test.conll.txt | sed '/^$/d' | awk '{print $2}' | sort | uniq | wc -l)

printf "Train\n"
printf "Sentences: $tr_sen\n"
printf "Tokens: $tr_tok\n"
printf "Tags: $tr_tag\n"
printf "\nTest\n"
printf "Sentences: $ts_sen\n"
printf "Tokens: $ts_tok\n"
printf "Tags: $ts_tag\n"
printf "\nUnseen\n"
printf "Tokens: $(($j_tok - $tr_tok))\n"
printf "Tags: $(($j_tag - $tr_tag))\n"