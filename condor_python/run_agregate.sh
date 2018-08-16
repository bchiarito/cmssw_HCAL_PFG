#! /bin/bash
hadd -f $1/summed_output_$2.root `ls -1 $1/* | grep 'output_run.*.root'`
cp $1/summed_output_$2.root .
