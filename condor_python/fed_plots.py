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
parser.add_option('--queue', type=int, action='store', dest='queue', help='for running with condor')
parser.add_option('--run', type=int, default=316110, action='store', dest='run', help='for running with condor')
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

#full he, hb
hist_he_totADCinTS_nocut = TH1F('hist_he_totADCinTS_nocut','hist_he_totADCinTS_nocut',8,0,8) 
hist_he_totADCinTS_cut10 = TH1F('hist_he_totADCinTS_cut10','hist_he_totADCinTS_cut10',8,0,8) 
hist_he_totADCinTS_cut15 = TH1F('hist_he_totADCinTS_cut15','hist_he_totADCinTS_cut15',8,0,8) 
hist_he_allADCinTS_nocut = TH2D('hist_he_allADCinTS_nocut','hist_he_allADCinTS_nocut',8,0,8,200,0,200) 
hist_he_allADCinTS_cut10 = TH2D('hist_he_allADCinTS_cut10','hist_he_allADCinTS_cut10',8,0,8,200,0,200) 
hist_he_allADCinTS_cut15 = TH2D('hist_he_allADCinTS_cut15','hist_he_allADCinTS_cut15',8,0,8,200,0,200) 

hist_hb_totADCinTS_nocut = TH1F('hist_hb_totADCinTS_nocut','hist_hb_totADCinTS_nocut',8,0,8) 
hist_hb_totADCinTS_cut5  = TH1F('hist_hb_totADCinTS_cut5' ,'hist_hb_totADCinTS_cut5' ,8,0,8) 
hist_hb_totADCinTS_cut8  = TH1F('hist_hb_totADCinTS_cut8' ,'hist_hb_totADCinTS_cut8' ,8,0,8)
hist_hb_allADCinTS_nocut = TH2D('hist_hb_allADCinTS_nocut','hist_hb_allADCinTS_nocut',8,0,8,150,0,150) 
hist_hb_allADCinTS_cut5  = TH2D('hist_hb_allADCinTS_cut5' ,'hist_hb_allADCinTS_cut5' ,8,0,8,150,0,150) 
hist_hb_allADCinTS_cut8  = TH2D('hist_hb_allADCinTS_cut8' ,'hist_hb_allADCinTS_cut8' ,8,0,8,150,0,150)
 
#proper fc plots for allgood, bad; proper fc plots for 12_414243good, bad; adc allgood, bad; full ho
hist_ho_totfCinTS_allgood = TH1F('hist_ho_totfCinTS_allgood','hist_ho_totfCinTS_allgood',10,0,10) 
hist_ho_totfCinTS_12_good = TH1F('hist_ho_totfCinTS_12_good','hist_ho_totfCinTS_12_good',10,0,10) 
hist_ho_totfCinTS_allbad  = TH1F('hist_ho_totfCinTS_allbad' ,'hist_ho_totfCinTS_allbad' ,10,0,10) 

hist_ho_totADCinTS_allgood = TH1F('hist_ho_totADCinTS_allgood','hist_ho_totADCinTS_allgood',10,0,10) 

hist_ho_totADCinTS_nocut = TH1F('hist_ho_totADCinTS_nocut','hist_ho_totADCinTS_nocut',10,0,10) 
hist_ho_totADCinTS_cut20 = TH1F('hist_ho_totADCinTS_cut20','hist_ho_totADCinTS_cut20',10,0,10) 
hist_ho_totADCinTS_cut15 = TH1F('hist_ho_totADCinTS_cut15','hist_ho_totADCinTS_cut15',10,0,10) 
hist_ho_allADCinTS_nocut = TH2D('hist_ho_allADCinTS_nocut','hist_ho_allADCinTS_nocut',10,0,10,150,0,150) 
hist_ho_allADCinTS_cut20 = TH2D('hist_ho_allADCinTS_cut20','hist_ho_allADCinTS_cut20',10,0,10,150,0,150) 
hist_ho_allADCinTS_cut15 = TH2D('hist_ho_allADCinTS_cut15','hist_ho_allADCinTS_cut15',10,0,10,150,0,150) 

#no cuts: ADC/TS measure for ho in each relevant channel
hist_ho_totADCinTS_nocut_12_40      = TH1F('hist_ho_totADCinTS_nocut_12_40',     'hist_ho_totADCinTS_nocut_12_40',10,0,10) #divide by below for avg
hist_ho_allADCinTS_nocut_12_40      = TH2D('hist_ho_allADCinTS_nocut_12_40',     'hist_ho_allADCinTS_nocut_12_40',10,0,10,150,0,150) #colz plot to see what goes into avg
hist_ho_totADCinTS_nocut_12_44      = TH1F('hist_ho_totADCinTS_nocut_12_44',     'hist_ho_totADCinTS_nocut_12_44',10,0,10)
hist_ho_allADCinTS_nocut_12_44      = TH2D('hist_ho_allADCinTS_nocut_12_44',     'hist_ho_allADCinTS_nocut_12_44',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_41_good = TH1F('hist_ho_totADCinTS_nocut_12_41_good','hist_ho_totADCinTS_nocut_12_41_good',10,0,10)
hist_ho_allADCinTS_nocut_12_41_good = TH2D('hist_ho_allADCinTS_nocut_12_41_good','hist_ho_allADCinTS_nocut_12_41_good',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_42_good = TH1F('hist_ho_totADCinTS_nocut_12_42_good','hist_ho_totADCinTS_nocut_12_42_good',10,0,10)
hist_ho_allADCinTS_nocut_12_42_good = TH2D('hist_ho_allADCinTS_nocut_12_42_good','hist_ho_allADCinTS_nocut_12_42_good',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_43_good = TH1F('hist_ho_totADCinTS_nocut_12_43_good','hist_ho_totADCinTS_nocut_12_43_good',10,0,10)
hist_ho_allADCinTS_nocut_12_43_good = TH2D('hist_ho_allADCinTS_nocut_12_43_good','hist_ho_allADCinTS_nocut_12_43_good',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_41_bad  = TH1F('hist_ho_totADCinTS_nocut_12_41_bad', 'hist_ho_totADCinTS_nocut_12_41_bad',10,0,10)
hist_ho_allADCinTS_nocut_12_41_bad  = TH2D('hist_ho_allADCinTS_nocut_12_41_bad', 'hist_ho_allADCinTS_nocut_12_41_bad',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_42_bad  = TH1F('hist_ho_totADCinTS_nocut_12_42_bad', 'hist_ho_totADCinTS_nocut_12_42_bad',10,0,10)
hist_ho_allADCinTS_nocut_12_42_bad  = TH2D('hist_ho_allADCinTS_nocut_12_42_bad', 'hist_ho_allADCinTS_nocut_12_42_bad',10,0,10,150,0,150)
hist_ho_totADCinTS_nocut_12_43_bad  = TH1F('hist_ho_totADCinTS_nocut_12_43_bad', 'hist_ho_totADCinTS_nocut_12_43_bad',10,0,10)
hist_ho_allADCinTS_nocut_12_43_bad  = TH2D('hist_ho_allADCinTS_nocut_12_43_bad', 'hist_ho_allADCinTS_nocut_12_43_bad',10,0,10,150,0,150)

#tight cuts: ho in each relevant channel
hist_ho_totADCinTS_cut20_12_40      = TH1F('hist_ho_totADCinTS_cut20_12_40',     'hist_ho_totADCinTS_cut20_12_40'     ,10,0,10)
hist_ho_allADCinTS_cut20_12_40      = TH2D('hist_ho_allADCinTS_cut20_12_40',     'hist_ho_allADCinTS_cut20_12_40'     ,10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_44      = TH1F('hist_ho_totADCinTS_cut20_12_44',     'hist_ho_totADCinTS_cut20_12_44'     ,10,0,10)
hist_ho_allADCinTS_cut20_12_44      = TH2D('hist_ho_allADCinTS_cut20_12_44',     'hist_ho_allADCinTS_cut20_12_44'     ,10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_41_good = TH1F('hist_ho_totADCinTS_cut20_12_41_good','hist_ho_totADCinTS_cut20_12_41_good',10,0,10)
hist_ho_allADCinTS_cut20_12_41_good = TH2D('hist_ho_allADCinTS_cut20_12_41_good','hist_ho_allADCinTS_cut20_12_41_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_42_good = TH1F('hist_ho_totADCinTS_cut20_12_42_good','hist_ho_totADCinTS_cut20_12_42_good',10,0,10)
hist_ho_allADCinTS_cut20_12_42_good = TH2D('hist_ho_allADCinTS_cut20_12_42_good','hist_ho_allADCinTS_cut20_12_42_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_43_good = TH1F('hist_ho_totADCinTS_cut20_12_43_good','hist_ho_totADCinTS_cut20_12_43_good',10,0,10)
hist_ho_allADCinTS_cut20_12_43_good = TH2D('hist_ho_allADCinTS_cut20_12_43_good','hist_ho_allADCinTS_cut20_12_43_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_41_bad  = TH1F('hist_ho_totADCinTS_cut20_12_41_bad', 'hist_ho_totADCinTS_cut20_12_41_bad' ,10,0,10)
hist_ho_allADCinTS_cut20_12_41_bad  = TH2D('hist_ho_allADCinTS_cut20_12_41_bad', 'hist_ho_allADCinTS_cut20_12_41_bad' ,10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_42_bad  = TH1F('hist_ho_totADCinTS_cut20_12_42_bad', 'hist_ho_totADCinTS_cut20_12_42_bad' ,10,0,10)
hist_ho_allADCinTS_cut20_12_42_bad  = TH2D('hist_ho_allADCinTS_cut20_12_42_bad', 'hist_ho_allADCinTS_cut20_12_42_bad' ,10,0,10,150,0,150)
hist_ho_totADCinTS_cut20_12_43_bad  = TH1F('hist_ho_totADCinTS_cut20_12_43_bad', 'hist_ho_totADCinTS_cut20_12_43_bad' ,10,0,10)
hist_ho_allADCinTS_cut20_12_43_bad  = TH2D('hist_ho_allADCinTS_cut20_12_43_bad', 'hist_ho_allADCinTS_cut20_12_43_bad' ,10,0,10,150,0,150)

#loose cuts: ho in each relevant channel
hist_ho_totADCinTS_cut15_12_40 = TH1F('hist_ho_totADCinTS_cut15_12_40','hist_ho_totADCinTS_cut15_12_40',10,0,10)
hist_ho_allADCinTS_cut15_12_40 = TH2D('hist_ho_allADCinTS_cut15_12_40','hist_ho_allADCinTS_cut15_12_40',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_44 = TH1F('hist_ho_totADCinTS_cut15_12_44','hist_ho_totADCinTS_cut15_12_44',10,0,10)
hist_ho_allADCinTS_cut15_12_44 = TH2D('hist_ho_allADCinTS_cut15_12_44','hist_ho_allADCinTS_cut15_12_44',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_41_good = TH1F('hist_ho_totADCinTS_cut15_12_41_good','hist_ho_totADCinTS_cut15_12_41_good',10,0,10)
hist_ho_allADCinTS_cut15_12_41_good = TH2D('hist_ho_allADCinTS_cut15_12_41_good','hist_ho_allADCinTS_cut15_12_41_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_42_good = TH1F('hist_ho_totADCinTS_cut15_12_42_good','hist_ho_totADCinTS_cut15_12_42_good',10,0,10)
hist_ho_allADCinTS_cut15_12_42_good = TH2D('hist_ho_allADCinTS_cut15_12_42_good','hist_ho_allADCinTS_cut15_12_42_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_43_good = TH1F('hist_ho_totADCinTS_cut15_12_43_good','hist_ho_totADCinTS_cut15_12_43_good',10,0,10)
hist_ho_allADCinTS_cut15_12_43_good = TH2D('hist_ho_allADCinTS_cut15_12_43_good','hist_ho_allADCinTS_cut15_12_43_good',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_41_bad = TH1F('hist_ho_totADCinTS_cut15_12_41_bad','hist_ho_totADCinTS_cut15_12_41_bad',10,0,10)
hist_ho_allADCinTS_cut15_12_41_bad = TH2D('hist_ho_allADCinTS_cut15_12_41_bad','hist_ho_allADCinTS_cut15_12_41_bad',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_42_bad = TH1F('hist_ho_totADCinTS_cut15_12_42_bad','hist_ho_totADCinTS_cut15_12_42_bad',10,0,10)
hist_ho_allADCinTS_cut15_12_42_bad = TH2D('hist_ho_allADCinTS_cut15_12_42_bad','hist_ho_allADCinTS_cut15_12_42_bad',10,0,10,150,0,150)
hist_ho_totADCinTS_cut15_12_43_bad = TH1F('hist_ho_totADCinTS_cut15_12_43_bad','hist_ho_totADCinTS_cut15_12_43_bad',10,0,10)
hist_ho_allADCinTS_cut15_12_43_bad = TH2D('hist_ho_allADCinTS_cut15_12_43_bad','hist_ho_allADCinTS_cut15_12_43_bad',10,0,10,150,0,150)

#how many adc counts in a 4TS sized pulse?
hist_ho_summedADC_soi0_12_414243_nocut_good = TH1F('hist_ho_summedADC_soi0_12_414243_nocut_good','hist_ho_summedADC_soi0_12_414243_nocut_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_nocut_good = TH1F('hist_ho_summedADC_soi4_12_414243_nocut_good','hist_ho_summedADC_soi4_12_414243_nocut_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_nocut_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_nocut_bad' ,'hist_ho_summedADC_soi0_12_414243_nocut_bad' ,600,0,600)
hist_ho_summedADC_soi4_12_414243_nocut_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_nocut_bad' ,'hist_ho_summedADC_soi4_12_414243_nocut_bad' ,600,0,600)
hist_ho_summedADC_soi0_12_414243_cut20_good = TH1F('hist_ho_summedADC_soi0_12_414243_cut20_good','hist_ho_summedADC_soi0_12_414243_cut20_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_cut20_good = TH1F('hist_ho_summedADC_soi4_12_414243_cut20_good','hist_ho_summedADC_soi4_12_414243_cut20_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_cut20_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_cut20_bad' ,'hist_ho_summedADC_soi0_12_414243_cut20_bad' ,600,0,600)
hist_ho_summedADC_soi4_12_414243_cut20_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_cut20_bad' ,'hist_ho_summedADC_soi4_12_414243_cut20_bad' ,600,0,600)
hist_ho_summedADC_soi0_12_414243_cut15_good = TH1F('hist_ho_summedADC_soi0_12_414243_cut15_good','hist_ho_summedADC_soi0_12_414243_cut15_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_cut15_good = TH1F('hist_ho_summedADC_soi4_12_414243_cut15_good','hist_ho_summedADC_soi4_12_414243_cut15_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_cut15_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_cut15_bad' ,'hist_ho_summedADC_soi0_12_414243_cut15_bad' ,600,0,600)
hist_ho_summedADC_soi4_12_414243_cut15_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_cut15_bad' ,'hist_ho_summedADC_soi4_12_414243_cut15_bad' ,600,0,600)

# individual branches to get
b_bx = array('I', [0])
chain.SetBranchAddress("bx", b_bx )

chain.SetBranchStatus('*',0)
chain.SetBranchStatus("bx", 1 )
chain.SetBranchStatus("HODigiIEta", 1 )
chain.SetBranchStatus("HODigiIPhi", 1 )
chain.SetBranchStatus("HODigiCapID", 1 )
chain.SetBranchStatus("HODigiADC", 1 )
chain.SetBranchStatus("HODigiFC", 1 )
chain.SetBranchStatus("QIE11DigiADC", 1 )
chain.SetBranchStatus("HBHEDigiADC", 1 )

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
  hits_ho = len(chain.HODigiADC)
  hits_he = len(chain.QIE11DigiADC)
  hits_hb = len(chain.HBHEDigiADC)
  ts_ho = 10
  ts_he = 8
  ts_hb = 8

  # HO PLOTS
  for i in range(hits_ho): #for every ho hit in the event:
    adc=[]
    fc=[]
    bad_hit = False
    tight = False
    loose = False
    sum_adc_soi0 = 0
    sum_adc_soi4 = 0
    eta = chain.HODigiIEta[i]
    phi = chain.HODigiIPhi[i]
    for j in range(ts_ho):
     adc.append(chain.HODigiADC[i][j])
     fc.append(chain.HODigiFC[i][j])
    
    if not ( (adc[4] - bx) % 4 == 1 ) : bad_hit = True
    if max(adc)>20: tight = True
    if max(adc)>15: loose = True
      
    for j in range(ts_ho): #fill plots
      if tight:
        if eta == 12:
          if phi == 40:
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totADCinTS_cut20_12_40.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20_12_40.Fill(j, adc[j])
          elif phi == 41:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut20_12_41_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_41_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut20_12_41_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_41_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
          elif phi == 42:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut20_12_42_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_42_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut20_12_42_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_42_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
          elif phi == 43:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut20_12_43_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_43_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut20_12_43_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut20_12_43_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
          elif phi == 44:
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totADCinTS_cut20_12_44.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20_12_44.Fill(j, adc[j])
          else: #if eta12 but not one of our phis
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
        else: #if not eta12
          hist_ho_totADCinTS_cut20.Fill(j, adc[j])
          hist_ho_allADCinTS_cut20.Fill(j, adc[j])
    
      if loose:
        if eta == 12:
          if phi == 40:
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totADCinTS_cut15_12_40.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15_12_40.Fill(j, adc[j])
          elif phi == 41:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut15_12_41_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_41_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut15_12_41_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_41_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
          elif phi == 42:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut15_12_42_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_42_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut15_12_42_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_42_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
          elif phi == 43:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            if bad_hit:
              hist_ho_totADCinTS_cut15_12_43_bad.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_43_bad.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
            else:
              hist_ho_totADCinTS_cut15_12_43_good.Fill(j, adc[j])
              hist_ho_allADCinTS_cut15_12_43_good.Fill(j, adc[j])
              hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
          elif phi == 44:
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totADCinTS_cut15_12_44.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15_12_44.Fill(j, adc[j])
          else: #if eta12 but not one of our phis
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
        else: #if not eta12
          hist_ho_totADCinTS_cut15.Fill(j, adc[j])
          hist_ho_allADCinTS_cut15.Fill(j, adc[j])

      if eta == 12: #if not tight or loose
        if phi == 40:
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, adc[j])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totADCinTS_nocut_12_40.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut_12_40.Fill(j, adc[j])
        elif phi == 41:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          if bad_hit:
            hist_ho_totfCinTS_allbad.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_41_bad.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_41_bad.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_12_good.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_41_good.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_41_good.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
        elif phi == 42:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          if bad_hit:
            hist_ho_totfCinTS_allbad.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_42_bad.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_42_bad.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_12_good.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_42_good.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_42_good.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
        elif phi == 43:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          if bad_hit:
            hist_ho_totfCinTS_allbad.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_43_bad.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_43_bad.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_12_good.Fill(j, adc[j])
            hist_ho_totADCinTS_nocut_12_43_good.Fill(j, adc[j])
            hist_ho_allADCinTS_nocut_12_43_good.Fill(j, adc[j])
            hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
            hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
        elif phi == 44:
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, adc[j])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totADCinTS_nocut_12_44.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut_12_44.Fill(j, adc[j])
        else: #if eta12 but not one of our phis
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, adc[j])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
      else: #if not eta12
        hist_ho_totADCinTS_allgood.Fill(j, adc[j])
        hist_ho_totfCinTS_allgood.Fill(j, adc[j])
        hist_ho_totADCinTS_nocut.Fill(j, adc[j])
        hist_ho_allADCinTS_nocut.Fill(j, adc[j])

  # HE PLOTS
  for i in range(hits_he): #for every he hit in the event:  
    adc=[]
    tight = False
    loose = False
    for j in range(ts_he):
     adc.append(chain.QIE11DigiADC[i][j])
    
    if max(adc)>15: tight = True
    if max(adc)>10: loose = True

    for j in range(ts_he):
      if tight:
        hist_he_totADCinTS_cut15.Fill(j, adc[j])
        hist_he_allADCinTS_cut15.Fill(j, adc[j])
      if loose:
        hist_he_totADCinTS_cut10.Fill(j, adc[j])
        hist_he_allADCinTS_cut10.Fill(j, adc[j])
      hist_he_totADCinTS_nocut.Fill(j, adc[j])
      hist_he_allADCinTS_nocut.Fill(j, adc[j])

  # HB PLOTS
  for i in range(hits_hb): #for every he hit in the event:  
    adc=[]
    tight = False
    loose = False
    for j in range(ts_hb):
     adc.append(chain.HBHEDigiADC[i][j])
    
    if max(adc)>8: tight = True
    if max(adc)>5: loose = True

    for j in range(ts_hb):
      if tight:
        hist_hb_totADCinTS_cut8.Fill(j, adc[j])
        hist_hb_allADCinTS_cut8.Fill(j, adc[j])
      if loose:
        hist_hb_totADCinTS_cut5.Fill(j, adc[j])
        hist_hb_allADCinTS_cut5.Fill(j, adc[j])
      hist_hb_totADCinTS_nocut.Fill(j, adc[j])
      hist_hb_allADCinTS_nocut.Fill(j, adc[j])

  count += 1
#  if count == 50: break

# Save file
out_file.cd()
out_file.Write()
out_file.Close()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
