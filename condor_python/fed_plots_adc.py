#Copies most logic from fed_plots.py; plots are made only for 'bad' channels (HO iEta +12, iPhi 41, 42, 43)
from __future__ import print_function
from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys, os, glob, fnmatch, time

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

#how many adc counts in a 4TS sized pulse?
hist_totalADC_ho_soi0_good = TH1F('hist_totalADC_ho_soi0_good','hist_totalADC_ho_soi0_good',600,0,600)
hist_totalADC_ho_soi4_good = TH1F('hist_totalADC_ho_soi4_good','hist_totalADC_ho_soi4_good',600,0,600)
hist_totalADC_ho_soi0_bad  = TH1F('hist_totalADC_ho_soi0_bad' ,'hist_totalADC_ho_soi0_bad',600,0,600)
hist_totalADC_ho_soi4_bad  = TH1F('hist_totalADC_ho_soi4_bad' ,'hist_totalADC_ho_soi4_bad',600,0,600)

#how many adc counts in each TS? overlay these
hist_ADC_ho_TS0 = TH1F('hist_ADC_ho_TS0','hist_ADC_ho_TS0',150,0,150)
hist_ADC_ho_TS1 = TH1F('hist_ADC_ho_TS1','hist_ADC_ho_TS1',150,0,150)
hist_ADC_ho_TS2 = TH1F('hist_ADC_ho_TS2','hist_ADC_ho_TS2',150,0,150)
hist_ADC_ho_TS3 = TH1F('hist_ADC_ho_TS3','hist_ADC_ho_TS3',150,0,150)
hist_ADC_ho_TS4 = TH1F('hist_ADC_ho_TS4','hist_ADC_ho_TS4',150,0,150)
hist_ADC_ho_TS5 = TH1F('hist_ADC_ho_TS5','hist_ADC_ho_TS5',150,0,150)
hist_ADC_ho_TS6 = TH1F('hist_ADC_ho_TS6','hist_ADC_ho_TS6',150,0,150)
hist_ADC_ho_TS7 = TH1F('hist_ADC_ho_TS7','hist_ADC_ho_TS7',150,0,150)
hist_ADC_ho_TS8 = TH1F('hist_ADC_ho_TS8','hist_ADC_ho_TS8',150,0,150)
hist_ADC_ho_TS9 = TH1F('hist_ADC_ho_TS9','hist_ADC_ho_TS9',150,0,150)

#2d maps: do ho pulses really always peak near the beginning?
hist_highestTSvstotADC_ho_bad  = TH2D('hist_highestTSvstotADC_ho_bad' ,'hist_highestTSvstotADC_ho_bad' ,10,0,10,1500,0,1500)
hist_highestTSvstotADC_ho_good = TH2D('hist_highestTSvstotADC_ho_good','hist_highestTSvstotADC_ho_good',10,0,10,1500,0,1500)
hist_highestTSvsADCinthatTS_ho_bad  = TH2D('hist_highestTSvsADCinthatTS_ho_bad' ,'hist_highestTSvsADCinthatTS_ho_bad' ,10,0,10,150,0,150)
hist_highestTSvsADCinthatTS_ho_good = TH2D('hist_highestTSvsADCinthatTS_ho_good','hist_highestTSvsADCinthatTS_ho_good',10,0,10,150,0,150)

#ho and he: average charge in each ts, to sort of get an 'average pulse'
hist_totADCinTS_ho_good = TH1F('hist_totADCinTS_ho_good', 'hist_totADCinTS_ho_good',10,0,10)
hist_totADCinTS_ho_bad = TH1F('hist_totADCinTS_ho_bad', 'hist_totADCinTS_ho_bad',10,0,10)
hist_totADCinTS_ho_cuts_good = TH1F('hist_totADCinTS_ho_cuts_good', 'hist_totADCinTS_ho_cuts_good',10,0,10)
hist_totADCinTS_ho_cuts_bad = TH1F('hist_totADCinTS_ho_cuts_bad', 'hist_totADCinTS_ho_cuts_bad',10,0,10)
hist_totninTS_ho_good = TH1D('hist_totninTS_ho_good','hist_totninTS_ho_good',10,0,10)
hist_totninTS_ho_bad  = TH1D('hist_totninTS_ho_bad' ,'hist_totninTS_ho_bad' ,10,0,10)
hist_totninTS_ho_cuts_good = TH1D('hist_totninTS_ho_cuts_good','hist_totninTS_ho_cuts_good',10,0,10)
hist_totninTS_ho_cuts_bad  = TH1D('hist_totninTS_ho_cuts_bad' ,'hist_totninTS_ho_cuts_bad' ,10,0,10)

hist_totADCinTS_ho = TH1F('hist_totADCinTS_ho', 'hist_totADCinTS_ho',10,0,10)
hist_totninTS_ho = TH1D('hist_totninTS_ho','hist_totninTS_ho',10,0,10)

hist_totADCinTS_hb = TH1F('hist_totADCinTS_hb', 'hist_totADCinTS_hb',8,0,8)
hist_totninTS_hb = TH1D('hist_totninTS_hb','hist_totninTS_hb',8,0,8)

hist_totADCinTS_he = TH1F('hist_totADCinTS_he', 'hist_totADCinTS_he',8,0,8)
hist_totninTS_he = TH1D('hist_totninTS_he','hist_totninTS_he',8,0,8)

#fancy colz pulse: what goes into that average above?
hist_allADCinTS_ho_bad  = TH2D('hist_allADCinTS_ho_bad' ,'hist_allADCinTS_ho_bad' ,10,0,10,150,0,150)
hist_allADCinTS_ho_good = TH2D('hist_allADCinTS_ho_good','hist_allADCinTS_ho_good',10,0,10,150,0,150)
hist_allADCinTS_ho      = TH2D('hist_allADCinTS_ho'     ,'hist_allADCinTS_ho'     ,10,0,10,150,0,150)
hist_allADCinTS_hb      = TH2D('hist_allADCinTS_hb'     ,'hist_allADCinTS_hb'     ,8,0,8,150,0,150)
hist_allADCinTS_he      = TH2D('hist_allADCinTS_he'     ,'hist_allADCinTS_he'     ,8,0,8,150,0,150)

# individual branches to get
b_bx = array('I', [0])
chain.SetBranchAddress("bx", b_bx )

chain.SetBranchStatus('*',0)
chain.SetBranchStatus("bx", 1 )
chain.SetBranchStatus("HODigiIEta", 1 )
chain.SetBranchStatus("HODigiIPhi", 1 )
chain.SetBranchStatus("HODigiCapID", 1 )
chain.SetBranchStatus("HODigiADC", 1 )
#chain.SetBranchStatus("QIE11DigiADC", 1 )
#chain.SetBranchStatus("HBHEDigiADC", 1 )

time_begin = time.time()
time_checkpoint = time.time()
count = 0
total = chain.GetEntries()
print_threshold = 0
print_increment = 10
while chain.GetEntry(count): #while you have events:

  # feedback to stdout
  percentDone = float(count+1) / float(total) * 100.0
  if percentDone > print_threshold:
    print('{0:10.1f} sec :'.format(time.time() - time_checkpoint), 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count+1, total, percentDone))
    time_checkpoint = time.time()
    print_threshold += print_increment

  bx = b_bx[0]

  # HO PLOTS
  for i in range(len(chain.HODigiCapID)): #for every ho hit in the event:
    for j in range(len(chain.HODigiCapID[i])): #make 'full ho' plots
      hist_totADCinTS_ho.Fill(j, chain.HODigiADC[i][j])
      hist_totninTS_ho.Fill(j)
      hist_allADCinTS_ho.Fill(j, chain.HODigiADC[i][j])

#    if not ( chain.HODigiIEta[i] == 12 and ( chain.HODigiIPhi[i] == 41 or chain.HODigiIPhi[i] == 42 or chain.HODigiIPhi[i] == 43 ) ): #if hit is not in one of the bad channels, skip to next hit
#      continue
#    
#    sum_adc_soi0 = 0
#    sum_adc_soi4 = 0
#    sum_adc = 0
#    bad_hit = False
#
#    hist_ADC_ho_TS0.Fill(chain.HODigiADC[i][0])
#    hist_ADC_ho_TS1.Fill(chain.HODigiADC[i][1])
#    hist_ADC_ho_TS2.Fill(chain.HODigiADC[i][2])
#    hist_ADC_ho_TS3.Fill(chain.HODigiADC[i][3])
#    hist_ADC_ho_TS4.Fill(chain.HODigiADC[i][4])
#    hist_ADC_ho_TS5.Fill(chain.HODigiADC[i][5])
#    hist_ADC_ho_TS6.Fill(chain.HODigiADC[i][6])
#    hist_ADC_ho_TS7.Fill(chain.HODigiADC[i][7])
#    hist_ADC_ho_TS8.Fill(chain.HODigiADC[i][8])
#    hist_ADC_ho_TS9.Fill(chain.HODigiADC[i][9])
#    
#    if not ( (chain.HODigiCapID[i][4] - bx) % 4 == 1) : bad_hit = True
#    highest_adc_in_ts = -100.0
#    highest_ts = -1
#    
#    for j in range(len(chain.HODigiCapID[i])): #for the 10 time slices
#      if not bad_hit: 
#        hist_totADCinTS_ho_good.Fill(j, chain.HODigiADC[i][j])
#        hist_allADCinTS_ho_good.Fill(j, chain.HODigiADC[i][j])
#        hist_totninTS_ho_good.Fill(j)
#      if bad_hit: 
#        hist_totADCinTS_ho_bad.Fill(j, chain.HODigiADC[i][j])
#        hist_allADCinTS_ho_bad.Fill(j, chain.HODigiADC[i][j])
#        hist_totninTS_ho_bad.Fill(j)
#      if chain.HODigiADC[i][j] > 9.0:
#        if not bad_hit: 
#          hist_totADCinTS_ho_cuts_good.Fill(j, chain.HODigiADC[i][j])
#          hist_totninTS_ho_cuts_good.Fill(j)
#        if bad_hit: 
#          hist_totADCinTS_ho_cuts_bad.Fill(j, chain.HODigiADC[i][j])
#          hist_totninTS_ho_cuts_bad.Fill(j)
#      
#      if (j >= 2 and j <= 5): sum_adc_soi4 += chain.HODigiADC[i][j]
#      if (j >= 0 and j <= 3): sum_adc_soi0 += chain.HODigiADC[i][j]
#      sum_adc += chain.HODigiADC[i][j]
#      if chain.HODigiADC[i][j] > highest_adc_in_ts:
#        highest_adc_in_ts = chain.HODigiADC[i][j]
#        highest_ts = j
#    
#    if bad_hit: 
#      hist_highestTSvstotADC_ho_bad.Fill(highest_ts, sum_adc)
#      hist_highestTSvsADCinthatTS_ho_bad.Fill(highest_ts, highest_adc_in_ts)
#    else: 
#      hist_highestTSvstotADC_ho_good.Fill(highest_ts, sum_adc)
#      hist_highestTSvsADCinthatTS_ho_good.Fill(highest_ts, highest_adc_in_ts)
#
#    if not bad_hit: hist_totalADC_ho_soi0_good.Fill(sum_adc_soi0)
#    if not bad_hit: hist_totalADC_ho_soi4_good.Fill(sum_adc_soi4)
#    if bad_hit: hist_totalADC_ho_soi0_bad.Fill(sum_adc_soi0)
#    if bad_hit: hist_totalADC_ho_soi4_bad.Fill(sum_adc_soi4)
    
#  # HE PLOTS
#  for i in range(len(chain.QIE11DigiADC)): #for every he hit in the event:  
#    for j in range(len(chain.QIE11DigiADC[i])):
#      hist_totADCinTS_he.Fill(j, chain.QIE11DigiADC[i][j])
#      hist_totninTS_he.Fill(j)
#      hist_allADCinTS_he.Fill(j, chain.QIE11DigiADC[i][j])
#
#  # HB PLOTS
#  for i in range(len(chain.HBHEDigiADC)): #for every he hit in the event:  
#    for j in range(len(chain.HBHEDigiADC[i])):
#      hist_totADCinTS_hb.Fill(j, chain.HBHEDigiADC[i][j])
#      hist_totninTS_hb.Fill(j)
#      hist_allADCinTS_hb.Fill(j, chain.HBHEDigiADC[i][j])

  count += 1
#  if count == 50: break

# Save file
out_file.cd()
out_file.Write()
out_file.Close()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
