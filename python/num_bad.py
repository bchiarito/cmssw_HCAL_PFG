from __future__ import print_function
from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch

import detector_map_functions as detmap

parser = OptionParser()
parser.add_option('--out',
                  dest='out', default="output.root",
                  help='output file')
parser.add_option('--tree',
                  dest='treename', default="hcalTupleTree/tree",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()

out_file = TFile(options.out, 'recreate')
in_file = args[0]

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(in_file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(in_file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

num_by_ls = TH1F('num_by_ls','num_by_ls',300,0,300)
num_by_event = TH1F('num_by_event','num_by_event',5000000,100000000,105000000)
num_by_bx = TH1F('num_by_bx','num_by_bx',3000,0,3000)

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
chain.SetBranchStatus("HODigiCapID", 1 )

count = 0
total = chain.GetEntries()
while chain.GetEntry(count):
  # feedback to stdout
  if count % 100 == 0:
    percentDone = float(count+1) / float(total) * 100.0
    print('Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count+1, total, percentDone ))

  ls = b_ls[0]
  bx = b_bx[0]
  event = b_event[0]

  num_by_ls.Fill(ls)
  num_by_event.Fill(event)
  num_by_bx.Fill(bx)

  for i in range(len(chain.HODigiCapID)):

    bad_hit = False
    if not ( (chain.HODigiCapID[i][4] - bx) % 4 == 1) : bad_hit = True

    if bad_hit:
      num_by_ls.Fill(ls)
      num_by_event.Fill(event)
      num_by_bx.Fill(bx)

  count += 1

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
