#!/usr/bin/env bash
OUT=$OUTFILE.out
echo $OUT
ERROR=$OUTFILE.err
echo $ERROR
./cmd1 < $INFILE | ./cmd3 1> $OUT 2> $ERROR

