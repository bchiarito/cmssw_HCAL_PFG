#! /bin/bash
hadd summed_output_run318974.root `ls -1 $PWD/* | grep output_run318974`
rm output_run318974*.root