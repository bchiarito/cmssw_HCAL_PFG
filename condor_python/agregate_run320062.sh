#! /bin/bash
hadd summed_output_run320062.root `ls -1 /uscms/homes/b/bchiari1/work/hcal/CMSSW_10_1_1/test/* | grep output_run320062`
rm output_run320062*.root
