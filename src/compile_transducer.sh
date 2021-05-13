#!/usr/bin/env bash

wdir='../w_dir'

fstcompile --isymbols=$wdir/isyms.txt --osymbols=$wdir/osyms.txt --keep_isymbols --keep_osymbols $wdir/w2t.txt $wdir/w2t.bin