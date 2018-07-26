from __future__ import print_function
from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch

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

NUM_ENTRIES = 3
NUM_EVENTS = 10

count = 0
total = chain.GetEntries()
for event in chain:
  count+=1
  percentDone = float(count) / float(total) * 100.0
  print('Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone ))

  print('Event', event.event, 'run', event.run, 'ls', event.ls, 'bx', event.bx, 'orbit', event.orbit, '\n')

  print('FEDs ::', len(event.FEDNumber), 'entries')
  print('=======')
  for i in range(len(event.FEDNumber)):
    print("Entry "+str(i+1)+":")
    print(' Number : '+str(event.FEDNumber[i]))
    print(' BCN : '+str(event.FEDBCN[i]))
    print(' Size : '+str(event.FEDSize[i]))
    print()
    if i == NUM_ENTRIES: break

  print('HBHE (HB) Entries ::', len(event.HBHEDigiIEta) ,'entries')
  print('==========')
  for i in range(len(event.HBHEDigiIEta)):
    print("Entry "+str(i+1)+":")
    print(' IEta : '+str(event.HBHEDigiIEta[i]))
    print(' IPhi : '+str(event.HBHEDigiIPhi[i]))
    print(' Depth : '+str(event.HBHEDigiDepth[i]))
    print(' RawID : '+str(event.HBHEDigiRawID[i]))
    print('CapIDs : ',end=' ')
    for j in range(len(event.HBHEDigiCapID[i])):
      print(event.HBHEDigiCapID[i][j],end=' ')
    print()
    print('ADCs : ',end=' ')
    for j in range(len(event.HBHEDigiADC[i])):
      print(event.HBHEDigiADC[i][j],end=' ')
    print()
    print('FCs : ',end=' ')
    for j in range(len(event.HBHEDigiFC[i])):
      print(event.HBHEDigiFC[i][j],end=' ')
    print()
    print()
    if i == NUM_ENTRIES: break

  print('QIE10 (HF) Entries ::', len(event.QIE10DigiIEta),'entries')
  print('=============')
  for i in range(len(event.QIE10DigiIEta)):
    print("Entry "+str(i+1)+":")
    print(' IEta : '+str(event.QIE10DigiIEta[i]))
    print(' IPhi : '+str(event.QIE10DigiIPhi[i]))
    print(' Depth : '+str(event.QIE10DigiDepth[i]))
    print(' RawID : '+str(event.QIE10DigiRawID[i]))
    print(' Flags : '+str(event.QIE10DigiFlags[i]))
    print('CapIDs : ',end=' ')
    for j in range(len(event.QIE10DigiCapID[i])):
      print(event.QIE10DigiCapID[i][j],end=' ')
    print()
    print('SOIs : ',end=' ')
    for j in range(len(event.QIE10DigiSOI[i])):
      print(event.QIE10DigiSOI[i][j],end=' ')
    print()
    print('ADCs : ',end=' ')
    print()
    for j in range(len(event.QIE10DigiADC[i])):
      print(event.QIE10DigiADC[i][j],end=' ')
    print()
    print('FCs : ',end=' ')
    for j in range(len(event.QIE10DigiFC[i])):
      print(event.HODigiFC[i][j],end=' ')
    print()
    print()
    if i == NUM_ENTRIES: break

  print('HO Entries ::', len(event.HODigiIEta), 'entries')
  print('==========')
  for i in range(len(event.HODigiIEta)):
    print("Entry "+str(i+1)+":")
    print(' IEta : '+str(event.HODigiIEta[i]))
    print(' IPhi : '+str(event.HODigiIPhi[i]))
    print(' Depth : '+str(event.HODigiDepth[i]))
    print(' RawID : '+str(event.HODigiRawID[i]))
    print('CapIDs : ',end=' ')
    for j in range(len(event.HODigiCapID[i])): print(event.HODigiCapID[i][j],end=' ')
    print()
    print('ADCs : ',end=' ')
    for j in range(len(event.HODigiADC[i])): print(event.HODigiADC[i][j],end=' ')
    print()
    print('FCs : ',end=' ')
    for j in range(len(event.HODigiFC[i])): print(event.HODigiFC[i][j],end=' ')
    print()
    print('AllFCs : ',end=' ')
    for j in range(len(event.HODigiAllFC[i])): print(event.HODigiAllFC[i][j],end=' ')
    print()
    print('Energys : ',end=' ')
    for j in range(len(event.HODigiEnergy[i])): print(event.HODigiEnergy[i][j],end=' ')
    print()
    print('Gains : ',end=' ')
    for j in range(len(event.HODigiGain[i])): print(event.HODigiGain[i][j],end=' ')
    print()
    print('NomFCs : ',end=' ')
    for j in range(len(event.HODigiNomFC[i])): print(event.HODigiNomFC[i][j],end=' ')
    print()
    print('PedFCs : ',end=' ')
    for j in range(len(event.HODigiPedFC[i])): print(event.HODigiPedFC[i][j],end=' ')
    print()
    print('RCGains : ',end=' ')
    for j in range(len(event.HODigiRCGain[i])): print(event.HODigiRCGain[i][j],end=' ')
    print()
    print('Raws : ',end=' ')
    for j in range(len(event.HODigiRaw[i])): print(event.HODigiRaw[i][j],end=' ')
    print()
    print('DVs : ',end=' ')
    for j in range(len(event.HODigiDV[i])): print(event.HODigiDV[i][j],end=' ')
    print()
    print('ERs : ',end=' ')
    for j in range(len(event.HODigiER[i])): print(event.HODigiER[i][j],end=' ')
    print()
    print('Fibers : ',end=' ')
    for j in range(len(event.HODigiFiber[i])): print(event.HODigiFiber[i][j],end=' ')
    print()
    print('FiberChans : ',end=' ')
    for j in range(len(event.HODigiFiberChan[i])): print(event.HODigiFiberChan[i][j],end=' ')
    print()
    print('LADCs : ',end=' ')
    for j in range(len(event.HODigiLADC[i])): print(event.HODigiLADC[i][j],end=' ')
    print()
    print()
    if i == NUM_ENTRIES: break

  print('QIE11 (HE) Entries ::', len(event.QIE11DigiIEta), 'entries')
  print('=============')
  for i in range(len(event.QIE11DigiIEta)):
    print("Entry "+str(i+1)+":")
    print(' IEta : '+str(event.QIE11DigiIEta[i]))
    print(' IPhi : '+str(event.QIE11DigiIPhi[i]))
    print(' CapIDError : '+str(event.QIE11DigiCapIDError[i]))
    print(' Subdet : '+str(event.QIE11DigiSubdet[i]))
    print(' Depth : '+str(event.QIE11DigiDepth[i]))
    print(' RawID : '+str(event.QIE11DigiRawID[i]))
    print(' LinkError : '+str(event.QIE11DigiLinkError[i]))
    print(' Flags : '+str(event.QIE11DigiFlags[i]))
    print(' NTDC : '+str(event.QIE11DigiNTDC[i]))
    print(' TimeFC : '+str(event.QIE11DigiTimeFC[i]))
    print(' TimeTDC : '+str(event.QIE11DigiTimeTDC[i]))
    print(' TotFC : '+str(event.QIE11DigiTotFC[i]))
    print('CapIDs : ',end=' ')
    for j in range(len(event.QIE11DigiCapID[i])):
      print(event.QIE11DigiCapID[i][j],end=' ')
    print()
    print('ADCs : ',end=' ')
    for j in range(len(event.QIE11DigiADC[i])):
      print(event.QIE11DigiADC[i][j],end=' ')
    print()
    print('FCs : ',end=' ')
    for j in range(len(event.QIE11DigiFC[i])):
      print(event.QIE11DigiFC[i][j],end=' ')
    print()
    print('TDCs : ',end=' ')
    for j in range(len(event.QIE11DigiTDC[i])):
      print(event.QIE11DigiTDC[i][j],end=' ')
    print()
    print('SOIs : ',end=' ')
    for j in range(len(event.QIE11DigiSOI[i])):
      print(event.QIE11DigiSOI[i][j],end=' ')
    print()
    print()
    if i == NUM_ENTRIES: break
  
  if count == NUM_EVENTS: break

print()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
