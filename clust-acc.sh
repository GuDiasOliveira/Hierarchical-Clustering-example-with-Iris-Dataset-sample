#!/bin/bash

echo -e "k\taccuracy"
for k in $(seq $1)
do
	acc=$(Rscript clustering.r $k && python accuracy.py)
	echo -e "$k\t$acc"
done
