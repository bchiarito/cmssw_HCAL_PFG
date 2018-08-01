from __future__ import print_function
from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch
import time

import detector_map_functions as detmap

parser = OptionParser()
parser.add_option('--out', dest='out', default="output.root", help='output file')
parser.add_option('--tree', dest='treename', default="hcalTupleTree/tree", help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False, dest='dir', help='treat file option as a directory instead of a single file')
parser.add_option('--queue', type=int, action='store', dest='queue', help='for running with conodr')
parser.add_option('--run', type=int, default=316110, action='store', dest='run', help='for running with conodr')
(options, args) = parser.parse_args()

input_files = ""
outputfilename = ""
if not options.queue == None:
  print('Got a queue number:', options.queue, 'and run:', options.run)
  input_files += "hcalTupleTree_"+str(options.queue)+".root"
  print("Using the file: ", input_files) 
  outputfilename = "output_run"+str(options.run)+"_"+str(options.queue)+".root"
else:
  input_files = args[0]
  outputfilename = options.out

out_file = TFile(outputfilename, 'recreate')

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(input_files)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(input_files):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

hist_FEDvsLS_total = TH2D('hist_FEDvsLS_total','Number of total hits',200,580,780,40,700,740)
hist_FEDvsLS_total.SetStats(0)
hist_FEDvsLS_total.GetXaxis().SetTitle('LS')
hist_FEDvsLS_total.GetYaxis().SetTitle('FED')

hist_FEDvsLS_bad = TH2D('hist_FEDvsLS_bad','Number of bad hits',200,580,780,40,700,740)
hist_FEDvsLS_bad.SetStats(0)
hist_FEDvsLS_bad.GetXaxis().SetTitle('LS')
hist_FEDvsLS_bad.GetYaxis().SetTitle('FED')

#print(detmap.loc_to_fed(5, 21, 4))

# individual branches to get
b_ls = array('I', [0])
b_bx = array('I', [0])
b_event = array('I', [0])

chain.SetBranchAddress("ls", b_ls )
chain.SetBranchAddress("bx", b_bx )
chain.SetBranchAddress("event", b_event )

chain.SetBranchStatus('*',0)
chain.SetBranchStatus("ls", 1 )
chain.SetBranchStatus("bx", 1 )
chain.SetBranchStatus("event", 1 )
chain.SetBranchStatus("HODigiIEta", 1 )
chain.SetBranchStatus("HODigiIPhi", 1 )
chain.SetBranchStatus("HODigiDepth", 1 )
chain.SetBranchStatus("HODigiCapID", 1 )

time_begin = time.time()
time_checkpoint = time.time()
count = 0
total = chain.GetEntries()
print_threshold = 0
print_increment = 10
while chain.GetEntry(count):
  # feedback to stdout
  percentDone = float(count+1) / float(total) * 100.0
  if percentDone > print_threshold:
    print('{0:10.1f} sec :'.format(time.time() - time_checkpoint), 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count+1, total, percentDone))
    time_checkpoint = time.time()
    print_threshold += print_increment

  ls = b_ls[0]
  bx = b_bx[0]
  event = b_event[0]

  for i in range(len(chain.HODigiIEta)):
    eta = chain.HODigiIEta[i]
    phi = chain.HODigiIPhi[i]
    depth = chain.HODigiDepth[i]
    feds = detmap.loc_to_fed(eta, phi, depth)

    bad_hit = False
    if not ( (chain.HODigiCapID[i][4] - bx) % 4 == 1) : bad_hit = True

    if len(feds) == 1:
      hist_FEDvsLS_total.Fill(bx, feds[0], 1)
      if bad_hit: hist_FEDvsLS_bad.Fill(bx, feds[0], 2)
    elif len(feds) == 2:
      hist_FEDvsLS_total.Fill(bx, feds[0], 0.5)
      if bad_hit: hist_FEDvsLS_bad.Fill(bx, feds[0], 0.5)
      hist_FEDvsLS_total.Fill(bx, feds[1], 0.5)
      if bad_hit: hist_FEDvsLS_bad.Fill(bx, feds[1], 0.5)
    else:
      print('three or more feds for a loc')

  count += 1

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
