#!/usr/bin/env bash

wdir='../w_dir'
tdir='../w_dir/test_dir'
mkdir $tdir

farcompilestrings --symbols=$wdir/isyms.txt --keep_symbols --unknown_symbol='<UNK>' $wdir/test.txt $wdir/test.far
farextract --filename_prefix="$tdir/" $wdir/test.far