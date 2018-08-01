#! /bin/bash
hadd summed_output_run316972.root `ls -1 /uscms/homes/b/bchiari1/work/hcal/CMSSW_10_1_1/test/* | grep output_run316972`
rm output_run316972*.root
