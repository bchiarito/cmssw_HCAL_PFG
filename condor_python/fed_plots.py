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

hist_FEDvsLS_total = TH2D('hist_FEDvsLS_total','Number of total hits',300,0,300,40,700,740)
hist_FEDvsLS_total.SetStats(0)
hist_FEDvsLS_total.GetXaxis().SetTitle('LS')
hist_FEDvsLS_total.GetYaxis().SetTitle('FED')

hist_FEDvsLS_bad = TH2D('hist_FEDvsLS_bad','Number of bad hits',300,0,300,40,700,740)
hist_FEDvsLS_bad.SetStats(0)
hist_FEDvsLS_bad.GetXaxis().SetTitle('LS')
hist_FEDvsLS_bad.GetYaxis().SetTitle('FED')

# set zeros
lumis = []
if options.run == 316110: lumis = range(1, 210)
elif options.run == 316972: lumis = range(1, 45)
elif options.run == 318974: lumis = range(1, 107)
elif options.run == 319629: lumis = range(1, 57)
elif options.run == 320062: lumis = range(1, 21)
else: lumis = range(1,1000)
ho_feds = range(724, 732)

for lumi in lumis:
  for ho_fed in ho_feds:
    hist_FEDvsLS_total.Fill(lumi, ho_fed, 1e-2)
    hist_FEDvsLS_bad.Fill(lumi, ho_fed, 1e-2)

hist_capcheck_ho = TH1F('hist_capcheck_ho','hist_capcheck_ho',4,0,4)
hist_capcheck_he = TH1F('hist_capcheck_he','hist_capcheck_he',4,0,4)
hist_capcheck_hf = TH1F('hist_capcheck_hf','hist_capcheck_hf',4,0,4)
hist_capcheck_hb = TH1F('hist_capcheck_hb','hist_capcheck_hb',4,0,4)

hist_avgfCvsTS_ho_good = TH1F('hist_avgfCvsTS_ho_good','hist_avgfCvsTS_ho_good',10,0,10)
hist_avgfCvsTS_ho_bad = TH1F('hist_avgfCvsTS_ho_bad','hist_avgfCvsTS_ho_bad',10,0,10)
hist_avgfCvsTS_he = TH1F('hist_avgfCvsTS_he','hist_avgfCvsTS_he',10,0,10)
hist_avgfCvsTS_hf = TH1F('hist_avgfCvsTS_hf','hist_avgfCvsTS_hf',10,0,10)
hist_avgfCvsTS_hb = TH1F('hist_avgfCvsTS_hb','hist_avgfCvsTS_hb',10,0,10)

hist_avgfCvsTS_cut_ho_good = TH1F('hist_avgfCvsTS_cut_ho_good','hist_avgfCvsTS_cut_ho_good',10,0,10)
hist_avgfCvsTS_cut_ho_bad = TH1F('hist_avgfCvsTS_cut_ho_bad','hist_avgfCvsTS_cut_ho_bad',10,0,10)
hist_avgfCvsTS_cut_he = TH1F('hist_avgfCvsTS_cut_he','hist_avgfCvsTS_cut_he',10,0,10)
hist_avgfCvsTS_cut_hf = TH1F('hist_avgfCvsTS_cut_hf','hist_avgfCvsTS_cut_hf',10,0,10)
hist_avgfCvsTS_cut_hb = TH1F('hist_avgfCvsTS_cut_hb','hist_avgfCvsTS_cut_hb',10,0,10)

hist_totalfC_ho_soi0_good = TH1F('hist_totalfC_ho_soi0_good','hist_totalfC_ho_soi0_good',200,0,100)
hist_totalfC_ho_soi4_good = TH1F('hist_totalfC_ho_soi4_good','hist_totalfC_ho_soi4_good',200,0,100)
hist_totalfC_ho_soi0_bad = TH1F('hist_totalfC_ho_soi0_bad','hist_totalfC_ho_soi0_bad',200,0,100)
hist_totalfC_ho_soi4_bad = TH1F('hist_totalfC_ho_soi4_bad','hist_totalfC_ho_soi4_bad',200,0,100)

hist_totalfC_he = TH1F('hist_totalfC_he','hist_totalfC_he',200,0,10000)
hist_totalfC_hb = TH1F('hist_totalfC_hb','hist_totalfC_hb',200,0,100)

hist_totalfC_ho_TS0 = TH1F('hist_totalfC_ho_TS0','hist_totalfC_ho_TS0',240,-10,50)
hist_totalfC_ho_TS1 = TH1F('hist_totalfC_ho_TS1','hist_totalfC_ho_TS1',240,-10,50)
hist_totalfC_ho_TS2 = TH1F('hist_totalfC_ho_TS2','hist_totalfC_ho_TS2',240,-10,50)
hist_totalfC_ho_TS3 = TH1F('hist_totalfC_ho_TS3','hist_totalfC_ho_TS3',240,-10,50)
hist_totalfC_ho_TS4 = TH1F('hist_totalfC_ho_TS4','hist_totalfC_ho_TS4',240,-10,50)
hist_totalfC_ho_TS5 = TH1F('hist_totalfC_ho_TS5','hist_totalfC_ho_TS5',240,-10,50)
hist_totalfC_ho_TS6 = TH1F('hist_totalfC_ho_TS6','hist_totalfC_ho_TS6',240,-10,50)
hist_totalfC_ho_TS7 = TH1F('hist_totalfC_ho_TS7','hist_totalfC_ho_TS7',240,-10,50)
hist_totalfC_ho_TS8 = TH1F('hist_totalfC_ho_TS8','hist_totalfC_ho_TS8',240,-10,50)
hist_totalfC_ho_TS9 = TH1F('hist_totalfC_ho_TS9','hist_totalfC_ho_TS9',240,-10,50)

hist_firstID_ho = TH1F('hist_firstID_ho','hist_firstID_ho',4,0,4)
hist_firstID_he = TH1F('hist_firstID_he','hist_firstID_he',4,0,4)
hist_firstID_hb = TH1F('hist_firstID_hb','hist_firstID_hb',4,0,4)
hist_firstID_hf = TH1F('hist_firstID_hf','hist_firstID_hf',4,0,4)

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
chain.SetBranchStatus("HBHEDigiCapID", 1 )
chain.SetBranchStatus("QIE11DigiCapID", 1 )
chain.SetBranchStatus("QIE10DigiCapID", 1 )
chain.SetBranchStatus("HODigiFC", 1 )
chain.SetBranchStatus("HBHEDigiFC", 1 )
chain.SetBranchStatus("QIE11DigiFC", 1 )
chain.SetBranchStatus("QIE10DigiFC", 1 )

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

  # fed vs LS plots
  for i in range(len(chain.HODigiIEta)):
    eta = chain.HODigiIEta[i]
    phi = chain.HODigiIPhi[i]
    depth = chain.HODigiDepth[i]
    feds = detmap.loc_to_fed(eta, phi, depth)
    bad_hit = False
    if not ( (chain.HODigiCapID[i][4] - bx) % 4 == 1) : bad_hit = True
    if len(feds) == 1:
      hist_FEDvsLS_total.Fill(ls, int(feds[0]), 1)
      if bad_hit: hist_FEDvsLS_bad.Fill(ls, int(feds[0]), 1)
    elif len(feds) == 2:
      hist_FEDvsLS_total.Fill(ls, int(feds[0]), 0.5)
      if bad_hit: hist_FEDvsLS_bad.Fill(ls, int(feds[0]), 0.5)
      hist_FEDvsLS_total.Fill(ls, int(feds[1]), 0.5)
      if bad_hit: hist_FEDvsLS_bad.Fill(ls, int(feds[1]), 0.5)
    else:
      print('three or more feds for a loc')

  # capid check plots
  # avg fC plots
  # total fC plots
  # first capID plots
  for i in range(len(chain.HODigiCapID)):
    hist_firstID_ho.Fill( chain.HODigiCapID[i][0] )
    sum_fc_soi0 = 0
    sum_fc_soi4 = 0
    hist_capcheck_ho.Fill((chain.HODigiCapID[i][4] - bx) % 4)
    bad_hit = False
    hist_totalfC_ho_TS0.Fill(chain.HODigiFC[i][0])
    hist_totalfC_ho_TS1.Fill(chain.HODigiFC[i][1])
    hist_totalfC_ho_TS2.Fill(chain.HODigiFC[i][2])
    hist_totalfC_ho_TS3.Fill(chain.HODigiFC[i][3])
    hist_totalfC_ho_TS4.Fill(chain.HODigiFC[i][4])
    hist_totalfC_ho_TS5.Fill(chain.HODigiFC[i][5])
    hist_totalfC_ho_TS6.Fill(chain.HODigiFC[i][6])
    hist_totalfC_ho_TS7.Fill(chain.HODigiFC[i][7])
    hist_totalfC_ho_TS8.Fill(chain.HODigiFC[i][8])
    hist_totalfC_ho_TS9.Fill(chain.HODigiFC[i][9])
    if not ( (chain.HODigiCapID[i][4] - bx) % 4 == 1) : bad_hit = True
    for j in range(len(chain.HODigiCapID[i])):
      if not bad_hit: hist_avgfCvsTS_ho_good.Fill(j, chain.HODigiFC[i][j])
      if     bad_hit: hist_avgfCvsTS_ho_bad.Fill(j, chain.HODigiFC[i][j])
      if chain.HODigiFC[i][j] > 1.0:
        if not bad_hit: hist_avgfCvsTS_cut_ho_good.Fill(j, chain.HODigiFC[i][j])
        if     bad_hit: hist_avgfCvsTS_cut_ho_bad.Fill(j, chain.HODigiFC[i][j])
      if (j >= 2 and j <= 5): sum_fc_soi4 += chain.HODigiFC[i][j]
      if (j >= 0 and j <= 3): sum_fc_soi0 += chain.HODigiFC[i][j]
    hist_totalfC_ho_soi0_good.Fill(sum_fc_soi0)
    hist_totalfC_ho_soi4_good.Fill(sum_fc_soi4)
    if bad_hit: hist_totalfC_ho_soi0_bad.Fill(sum_fc_soi0)
    if bad_hit: hist_totalfC_ho_soi4_bad.Fill(sum_fc_soi4)

  for i in range(len(chain.QIE11DigiCapID)):
    hist_firstID_he.Fill( chain.QIE11DigiCapID[i][0] )
    sum_fc = 0
    hist_capcheck_he.Fill((chain.QIE11DigiCapID[i][3] - bx) % 4)
    for j in range(len(chain.QIE11DigiCapID[i])):
      hist_avgfCvsTS_he.Fill(j, chain.QIE11DigiFC[i][j])
      if chain.QIE11DigiFC[i][j] > 1.0: hist_avgfCvsTS_cut_he.Fill(j, chain.QIE11DigiFC[i][j])  
      if (j >= 1 and j <= 4): sum_fc += chain.QIE11DigiFC[i][j]
    hist_totalfC_he.Fill(sum_fc)

  for i in range(len(chain.QIE10DigiCapID)):
    hist_firstID_hf.Fill( chain.QIE10DigiCapID[i][0] )
    hist_capcheck_hf.Fill((chain.QIE10DigiCapID[i][1] - bx) % 4)
    for j in range(len(chain.QIE10DigiCapID[i])):
      hist_avgfCvsTS_hf.Fill(j, chain.QIE10DigiFC[i][j])
      if chain.QIE10DigiFC[i][j] > 1.0: hist_avgfCvsTS_cut_hf.Fill(j, chain.QIE10DigiFC[i][j])

  for i in range(len(chain.HBHEDigiCapID)):
    hist_firstID_hb.Fill( chain.HBHEDigiCapID[i][0] )
    sum_fc = 0
    hist_capcheck_hb.Fill((chain.HBHEDigiCapID[i][3] - bx) % 4)
    for j in range(len(chain.HBHEDigiCapID[i])):
      hist_avgfCvsTS_hb.Fill(j, chain.HBHEDigiFC[i][j])
      if chain.HBHEDigiFC[i][j] > 1.0: hist_avgfCvsTS_cut_hb.Fill(j, chain.HBHEDigiFC[i][j])
      if (j >= 1 and j <= 4): sum_fc += chain.HBHEDigiFC[i][j]
    hist_totalfC_hb.Fill(sum_fc)

  count += 1

hist_avgfCvsTS_ho_good.Scale(10.0 / hist_avgfCvsTS_ho_good.GetEntries())
hist_avgfCvsTS_ho_bad.Scale(10.0 / hist_avgfCvsTS_ho_bad.GetEntries())
hist_avgfCvsTS_he.Scale(8.0 / hist_avgfCvsTS_he.GetEntries())
hist_avgfCvsTS_hf.Scale(3.0 / hist_avgfCvsTS_hf.GetEntries()) 
hist_avgfCvsTS_hb.Scale(8.0 / hist_avgfCvsTS_hb.GetEntries()) 

hist_FEDvsLS_fracbad = TH2D('hist_FEDvsLS_fracbad','Fraction of total hits',300,0,300,40,700,740)
hist_FEDvsLS_fracbad.Add(hist_FEDvsLS_bad)
hist_FEDvsLS_fracbad.Divide(hist_FEDvsLS_total)
hist_FEDvsLS_fracbad.SetStats(0)
hist_FEDvsLS_fracbad.GetXaxis().SetTitle('LS')
hist_FEDvsLS_fracbad.GetYaxis().SetTitle('FED')

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
