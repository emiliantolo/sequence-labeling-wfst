#!/usr/bin/env bash

wdir='../w_dir'

ngramsymbols $wdir/words.txt $wdir/isyms.txt
ngramsymbols $wdir/tags.txt $wdir/osyms.txt