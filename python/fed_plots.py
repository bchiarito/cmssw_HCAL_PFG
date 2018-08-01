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

hist_FEDvsLS_total = TH2D('hist_FEDvsLS_total','Number of total hits',200,580,780,40,700,740)
hist_FEDvsLS_total.SetStats(0)
hist_FEDvsLS_total.GetXaxis().SetTitle('LS')
hist_FEDvsLS_total.GetYaxis().SetTitle('FED')

hist_FEDvsLS_bad = TH2D('hist_FEDvsLS_bad','Number of bad hits',200,580,780,40,700,740)
hist_FEDvsLS_bad.SetStats(0)
hist_FEDvsLS_bad.GetXaxis().SetTitle('LS')
hist_FEDvsLS_bad.GetYaxis().SetTitle('FED')

print(detmap.loc_to_fed(5, 21, 4))


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

c = TCanvas()
c.SetLogz()
hist_FEDvsLS_total.Draw('Colz')
raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
