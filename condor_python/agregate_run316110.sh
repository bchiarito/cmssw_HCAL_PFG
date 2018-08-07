#! /bin/bash
hadd -f summed_output_run316110.root `ls -1 $PWD/* | grep output_run316110`
rm output_run316110*.root
