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
xrdcp --nopbar root://cmseos.fnal.gov//store/user/bchiari1/noreplica/hcal/task9/multirun_allbadcapid/ZeroBias/hcaltuple_run319629/180724_151527/0000/hcalTupleTree_$1.root .
echo 'now trying python with:' $1 $2
python fed_plots.py --queue=$1 --run=319629
rm hcalTupleTree_$1.root
