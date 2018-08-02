#! /bin/bash
hadd summed_output_run319629.root `ls -1 $PWD/* | grep output_run319629`
rm output_run319629*.root
