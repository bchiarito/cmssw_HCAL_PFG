#! /bin/bash
echo 'I am here'
pwd
ls
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
eval `scramv1 project CMSSW CMSSW_10_1_1`
cd CMSSW_10_1_1/src
eval `scramv1 runtime -sh`
echo "CMSSW: "$CMSSW_BASE
cd ../..
echo "copying file with xrdcp"
xrdcp --nopbar $3/hcalTupleTree_$1.root .
echo 'now trying python with:' $1
python fed_plots.py --queue=$1 --run=$2
rm hcalTupleTree_$1.root
