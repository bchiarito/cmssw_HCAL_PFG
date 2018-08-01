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
xrdcp --nopbar root://cmseos.fnal.gov//store/user/bchiari1/noreplica/hcal/task9/run316110/ZeroBias/hcaltuple_run316110/180720_125806/0000/hcalTupleTree_$1.root .
echo 'now trying python with:' $1
python capid_checker.py --queue=$1
rm hcalTupleTree_$1.root
