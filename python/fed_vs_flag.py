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
parser.add_option('--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree',
                  dest='treename', default="hcalTupleTree/tree",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()

out_file = TFile(options.out, 'recreate')

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(options.file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

hist_fedvsflag = TH2D('hist_fedvsflag','FED vs Flag for all hits',7000,0,70000,150,0,1500)
hist_fedvsflag.SetStats(0)
hist_fedvsflag.GetXaxis().SetTitle('flag')
hist_fedvsflag.GetYaxis().SetTitle('FED')

print(detmap.loc_to_fed(5, 21, 4))

count = 0
total = chain.GetEntries()
for event in chain:
  count += 1
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print('Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone ))

  for i in range(len(event.QIE11DigiIEta)):
    flag = event.QIE11DigiFlags[i]
    eta = event.QIE11DigiIEta[i]
    phi = event.QIE11DigiIPhi[i]
    depth = event.QIE11DigiDepth[i]
    if abs(eta) > 14: continue
    print(eta)
    feds = detmap.loc_to_fed(eta, phi, depth)
    if len(feds) == 1:
      hist_fedvsflag.Fill(flag, feds[0], 2)
    elif len(feds) == 2:
      hist_fedvsflag.Fill(flag, feds[0])
      hist_fedvsflag.Fill(flag, feds[1])
    else:
      print('three or more feds for a loc')

  if count == -1: break

c = TCanvas()
c.SetLogz()
hist_fedvsflag.Draw('LEGO0')
raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
