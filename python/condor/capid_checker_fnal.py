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
#import detector_map_functions as detmap

parser = OptionParser()
parser.add_option('--out', dest='out', default="output.root", help='output file')
parser.add_option('--tree', dest='treename', default="hcalTupleTree/tree", help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False, dest='dir', help='treat file option as a directory instead of a single file')
parser.add_option('--queue', type=int, action='store', dest='queue', help='for running with conodr')
parser.add_option('--run', type=int, default=316110, action='store', dest='run', help='for running with conodr')
(options, args) = parser.parse_args()

input_files = ""
if not options.queue == None:
  print('Got a queue number:', options.queue)
  input_files += "hcalTupleTree_"+str(options.queue)+".root"
  print("Using the file: ", input_files) 
else:
  input_files = args[0]

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

print_increment = 5

time_begin = time.time()
time_checkpoint = time.time()
count = 0
total = chain.GetEntries()
print_threshold = 0
for event in chain:
  count+=1
  percentDone = float(count) / float(total) * 100.0
  if percentDone > print_threshold:
  #if count == 1 or count % 100 == 0:
    print('{0:10.1f} sec :'.format(time.time() - time_checkpoint), 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone))
    time_checkpoint = time.time()
    print_threshold += print_increment

  for i in range(len(event.HODigiIEta)):
    bad_rotation = False
    for j in range(len(event.HODigiCapID[i])):
      if j == 0: continue
      cur = event.HODigiCapID[i][j]
      prev = event.HODigiCapID[i][j-1]
      if   cur == 0 and prev == 3: bad_rotation = False
      elif cur == 1 and prev == 0: bad_rotation = False
      elif cur == 2 and prev == 1: bad_rotation = False
      elif cur == 3 and prev == 2: bad_rotation = False
      else: bad_rotation = True

    if bad_rotation:
      print ('found a bad rotation in event ', event.event, 'ls', event.ls, 'run', event.run)
      print('CapIDs : ',end=' ')
      for j in range(len(event.HODigiCapID[i])): print(event.HODigiCapID[i][j],end=' ') 
      print(' IEta : '+str(event.HODigiIEta[i]))
      print(' IPhi : '+str(event.HODigiIPhi[i]))
      print(' Depth : '+str(event.HODigiDepth[i]))
      print(' RawID : '+str(event.HODigiRawID[i]))
      eta = event.HODigiIEta[i]
      phi = event.HODigiIPhi[i]
      depth = event.HODigiDepth[i]
      feds = detmap.loc_to_fed(eta, phi, depth)
      print('FED :', feds)
      print()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
