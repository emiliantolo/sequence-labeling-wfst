#!/usr/bin/env bash

wdir='../w_dir'
tdir='../w_dir/test_dir'
farr=($(ls $tdir))

for f in ${farr[@]}
do
    fstcompose $tdir/$f $wdir/w2t.bin | fstcompose - $wdir/m.lm | fstshortestpath | fstrmepsilon | fsttopsort | fstprint --isymbols=$wdir/isyms.txt
done > $wdir/w2t_m.out