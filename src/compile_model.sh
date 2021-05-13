#!/usr/bin/env bash

wdir='../w_dir'
order=$1
method=$2

farcompilestrings --symbols=$wdir/osyms.txt --keep_symbols --unknown_symbol='<UNK>' $wdir/train.tags.txt $wdir/train.tags.far
ngramcount --order=$order $wdir/train.tags.far $wdir/train.tags.cnt
ngrammake --method=$method $wdir/train.tags.cnt $wdir/m.lm