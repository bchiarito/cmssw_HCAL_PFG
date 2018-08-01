#! /bin/bash
echo 'I am here'
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /users/h2/chiarito/scratch/CMSSW_10_1_1/src
eval `scramv1 runtime -sh`
cd /cms/chiarito/work/hcal/CMSSW_10_1_1/test
echo 'now trying python with:'
echo $1
echo $2
python capid_checker.py --queue=$1 --run=$2
