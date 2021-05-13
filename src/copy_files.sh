#!/usr/bin/env bash

dpath='../data/NL2SparQL4NLU'
wdir='../w_dir'

rm -r $wdir
mkdir $wdir

cp $dpath.train.utterances.txt $wdir/train.txt
cp $dpath.test.utterances.txt $wdir/test.txt

cp $dpath.train.conll.txt $wdir/train.conll
cp $dpath.test.conll.txt $wdir/test.conll