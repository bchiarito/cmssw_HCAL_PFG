#! /bin/bash
hadd summed_output_run316972.root `ls -1 $PWD/* | grep output_run316972`
rm output_run316972*.root
