#! /bin/bash
hadd summed_output_run316110.root `ls -1 $PWD/* | grep output_run316110`
rm output_run316110*.root
