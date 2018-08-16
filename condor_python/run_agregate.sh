#! /bin/bash
hadd -f $1/summed_output.root `ls -1 $1/* | grep output_run`
