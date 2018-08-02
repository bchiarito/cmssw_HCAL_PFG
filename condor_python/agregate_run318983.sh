#! /bin/bash
hadd summed_output_run318983.root `ls -1 $PWD/* | grep output_run318983`
rm output_run318983*.root
