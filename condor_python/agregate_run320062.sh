#! /bin/bash
hadd summed_output_run320062.root `ls -1 $PWD/* | grep output_run320062`
rm output_run320062*.root
