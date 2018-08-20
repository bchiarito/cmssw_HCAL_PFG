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

hist_he_totfCinTS_nocut = TH1F('hist_he_totfCinTS_nocut','hist_he_totfCinTS_nocut',8,0,8) 
hist_he_totfCinTS_cut10 = TH1F('hist_he_totfCinTS_cut10','hist_he_totfCinTS_cut10',8,0,8) 
hist_he_totfCinTS_cut15 = TH1F('hist_he_totfCinTS_cut15','hist_he_totfCinTS_cut15',8,0,8)

hist_he_allADCinTS_nocut = TH2D('hist_he_allADCinTS_nocut','hist_he_allADCinTS_nocut',8,0,8,200,0,200)
hist_he_allADCinTS_cut10 = TH2D('hist_he_allADCinTS_cut10','hist_he_allADCinTS_cut10',8,0,8,200,0,200)
hist_he_allADCinTS_cut15 = TH2D('hist_he_allADCinTS_cut15','hist_he_allADCinTS_cut15',8,0,8,200,0,200)

hist_he_allfCinTS_nocut = TH2D('hist_he_allfCinTS_nocut','hist_he_allfCinTS_nocut',8,0,8,10000,-1000,9000)
hist_he_allfCinTS_cut10 = TH2D('hist_he_allfCinTS_cut10','hist_he_allfCinTS_cut10',8,0,8,10000,-1000,9000)
hist_he_allfCinTS_cut15 = TH2D('hist_he_allfCinTS_cut15','hist_he_allfCinTS_cut15',8,0,8,10000,-1000,9000)

hist_hb_totADCinTS_nocut = TH1F('hist_hb_totADCinTS_nocut','hist_hb_totADCinTS_nocut',8,0,8) 
hist_hb_totADCinTS_cut5  = TH1F('hist_hb_totADCinTS_cut5' ,'hist_hb_totADCinTS_cut5' ,8,0,8) 
hist_hb_totADCinTS_cut8  = TH1F('hist_hb_totADCinTS_cut8' ,'hist_hb_totADCinTS_cut8' ,8,0,8)

hist_hb_totfCinTS_nocut = TH1F('hist_hb_totfCinTS_nocut','hist_hb_totfCinTS_nocut',8,0,8) 
hist_hb_totfCinTS_cut5  = TH1F('hist_hb_totfCinTS_cut5' ,'hist_hb_totfCinTS_cut5' ,8,0,8) 
hist_hb_totfCinTS_cut8  = TH1F('hist_hb_totfCinTS_cut8' ,'hist_hb_totfCinTS_cut8' ,8,0,8)

hist_hb_allADCinTS_nocut = TH2D('hist_hb_allADCinTS_nocut','hist_hb_allADCinTS_nocut',8,0,8,150,0,150)
hist_hb_allADCinTS_cut5  = TH2D('hist_hb_allADCinTS_cut5' ,'hist_hb_allADCinTS_cut5' ,8,0,8,150,0,150)
hist_hb_allADCinTS_cut8  = TH2D('hist_hb_allADCinTS_cut8' ,'hist_hb_allADCinTS_cut8' ,8,0,8,150,0,150)

hist_hb_allfCinTS_nocut = TH2D('hist_hb_allfCinTS_nocut','hist_hb_allfCinTS_nocut',8,0,8,10000,-1000,9000)
hist_hb_allfCinTS_cut5  = TH2D('hist_hb_allfCinTS_cut5' ,'hist_hb_allfCinTS_cut5' ,8,0,8,10000,-1000,9000)
hist_hb_allfCinTS_cut8  = TH2D('hist_hb_allfCinTS_cut8' ,'hist_hb_allfCinTS_cut8' ,8,0,8,10000,-1000,9000)
 
#full ho; misc ho plots (proper fc plots for allgood, bad; proper fc plots for 12_414243good, bad; adc allgood, bad)
hist_ho_totADCinTS_nocut = TH1F('hist_ho_totADCinTS_nocut','hist_ho_totADCinTS_nocut',10,0,10) 
hist_ho_totADCinTS_cut15 = TH1F('hist_ho_totADCinTS_cut15','hist_ho_totADCinTS_cut15',10,0,10) 
hist_ho_totADCinTS_cut20 = TH1F('hist_ho_totADCinTS_cut20','hist_ho_totADCinTS_cut20',10,0,10) 

hist_ho_totfCinTS_nocut = TH1F('hist_ho_totfCinTS_nocut','hist_ho_totfCinTS_nocut',10,0,10) 
hist_ho_totfCinTS_cut15 = TH1F('hist_ho_totfCinTS_cut15','hist_ho_totfCinTS_cut15',10,0,10) 
hist_ho_totfCinTS_cut20 = TH1F('hist_ho_totfCinTS_cut20','hist_ho_totfCinTS_cut20',10,0,10) 

hist_ho_allADCinTS_nocut = TH2D('hist_ho_allADCinTS_nocut','hist_ho_allADCinTS_nocut',10,0,10,150,0,150)
hist_ho_allADCinTS_cut15 = TH2D('hist_ho_allADCinTS_cut15','hist_ho_allADCinTS_cut15',10,0,10,150,0,150)
hist_ho_allADCinTS_cut20 = TH2D('hist_ho_allADCinTS_cut20','hist_ho_allADCinTS_cut20',10,0,10,150,0,150)

hist_ho_allfCinTS_nocut = TH2D('hist_ho_allfCinTS_nocut','hist_ho_allfCinTS_nocut',10,0,10,10000,-1000,9000)
hist_ho_allfCinTS_cut15 = TH2D('hist_ho_allfCinTS_cut15','hist_ho_allfCinTS_cut15',10,0,10,10000,-1000,9000)
hist_ho_allfCinTS_cut20 = TH2D('hist_ho_allfCinTS_cut20','hist_ho_allfCinTS_cut20',10,0,10,10000,-1000,9000)

hist_ho_totfCinTS_allgood = TH1F('hist_ho_totfCinTS_allgood','hist_ho_totfCinTS_allgood',10,0,10) 
hist_ho_totADCinTS_allgood = TH1F('hist_ho_totADCinTS_allgood','hist_ho_totADCinTS_allgood',10,0,10) 

hist_ho_numbadperls = TH1F('hist_ho_numbadperls','hist_ho_numbadperls',600,0,600) 
hist_ho_numtotperls = TH1F('hist_ho_numtotperls','hist_ho_numtotperls',600,0,600) 

hist_ho_badhits_etaphi = TH2D('hist_ho_badhits_etaphi','hist_ho_badhits_etaphi',40,-20,20,90,0,90)

#no cuts: ADC and fC/TS measure for ho in each relevant channel
hist_ho_totADCinTS_nocut_12_40      = TH1F('hist_ho_totADCinTS_nocut_12_40',     'hist_ho_totADCinTS_nocut_12_40',10,0,10) 
hist_ho_totADCinTS_nocut_12_44      = TH1F('hist_ho_totADCinTS_nocut_12_44',     'hist_ho_totADCinTS_nocut_12_44',10,0,10)
hist_ho_totADCinTS_nocut_12_41_good = TH1F('hist_ho_totADCinTS_nocut_12_41_good','hist_ho_totADCinTS_nocut_12_41_good',10,0,10)
hist_ho_totADCinTS_nocut_12_42_good = TH1F('hist_ho_totADCinTS_nocut_12_42_good','hist_ho_totADCinTS_nocut_12_42_good',10,0,10)
hist_ho_totADCinTS_nocut_12_43_good = TH1F('hist_ho_totADCinTS_nocut_12_43_good','hist_ho_totADCinTS_nocut_12_43_good',10,0,10)
hist_ho_totADCinTS_nocut_12_41_bad  = TH1F('hist_ho_totADCinTS_nocut_12_41_bad', 'hist_ho_totADCinTS_nocut_12_41_bad',10,0,10)
hist_ho_totADCinTS_nocut_12_42_bad  = TH1F('hist_ho_totADCinTS_nocut_12_42_bad', 'hist_ho_totADCinTS_nocut_12_42_bad',10,0,10)
hist_ho_totADCinTS_nocut_12_43_bad  = TH1F('hist_ho_totADCinTS_nocut_12_43_bad', 'hist_ho_totADCinTS_nocut_12_43_bad',10,0,10)

hist_ho_totfCinTS_nocut_12_40      = TH1F('hist_ho_totfCinTS_nocut_12_40',     'hist_ho_totfCinTS_nocut_12_40',10,0,10) 
hist_ho_totfCinTS_nocut_12_44      = TH1F('hist_ho_totfCinTS_nocut_12_44',     'hist_ho_totfCinTS_nocut_12_44',10,0,10)
hist_ho_totfCinTS_nocut_12_41_good = TH1F('hist_ho_totfCinTS_nocut_12_41_good','hist_ho_totfCinTS_nocut_12_41_good',10,0,10)
hist_ho_totfCinTS_nocut_12_42_good = TH1F('hist_ho_totfCinTS_nocut_12_42_good','hist_ho_totfCinTS_nocut_12_42_good',10,0,10)
hist_ho_totfCinTS_nocut_12_43_good = TH1F('hist_ho_totfCinTS_nocut_12_43_good','hist_ho_totfCinTS_nocut_12_43_good',10,0,10)
hist_ho_totfCinTS_nocut_12_41_bad  = TH1F('hist_ho_totfCinTS_nocut_12_41_bad', 'hist_ho_totfCinTS_nocut_12_41_bad',10,0,10)
hist_ho_totfCinTS_nocut_12_42_bad  = TH1F('hist_ho_totfCinTS_nocut_12_42_bad', 'hist_ho_totfCinTS_nocut_12_42_bad',10,0,10)
hist_ho_totfCinTS_nocut_12_43_bad  = TH1F('hist_ho_totfCinTS_nocut_12_43_bad', 'hist_ho_totfCinTS_nocut_12_43_bad',10,0,10)

#loose cuts: ho in each relevant channel
hist_ho_totADCinTS_cut15_12_40      = TH1F('hist_ho_totADCinTS_cut15_12_40',     'hist_ho_totADCinTS_cut15_12_40',10,0,10)
hist_ho_totADCinTS_cut15_12_44      = TH1F('hist_ho_totADCinTS_cut15_12_44',     'hist_ho_totADCinTS_cut15_12_44',10,0,10)
hist_ho_totADCinTS_cut15_12_41_good = TH1F('hist_ho_totADCinTS_cut15_12_41_good','hist_ho_totADCinTS_cut15_12_41_good',10,0,10)
hist_ho_totADCinTS_cut15_12_42_good = TH1F('hist_ho_totADCinTS_cut15_12_42_good','hist_ho_totADCinTS_cut15_12_42_good',10,0,10)
hist_ho_totADCinTS_cut15_12_43_good = TH1F('hist_ho_totADCinTS_cut15_12_43_good','hist_ho_totADCinTS_cut15_12_43_good',10,0,10)
hist_ho_totADCinTS_cut15_12_41_bad  = TH1F('hist_ho_totADCinTS_cut15_12_41_bad', 'hist_ho_totADCinTS_cut15_12_41_bad',10,0,10)
hist_ho_totADCinTS_cut15_12_42_bad  = TH1F('hist_ho_totADCinTS_cut15_12_42_bad', 'hist_ho_totADCinTS_cut15_12_42_bad',10,0,10)
hist_ho_totADCinTS_cut15_12_43_bad  = TH1F('hist_ho_totADCinTS_cut15_12_43_bad', 'hist_ho_totADCinTS_cut15_12_43_bad',10,0,10)

hist_ho_totfCinTS_cut15_12_40      = TH1F('hist_ho_totfCinTS_cut15_12_40',     'hist_ho_totfCinTS_cut15_12_40',10,0,10)
hist_ho_totfCinTS_cut15_12_44      = TH1F('hist_ho_totfCinTS_cut15_12_44',     'hist_ho_totfCinTS_cut15_12_44',10,0,10)
hist_ho_totfCinTS_cut15_12_41_good = TH1F('hist_ho_totfCinTS_cut15_12_41_good','hist_ho_totfCinTS_cut15_12_41_good',10,0,10)
hist_ho_totfCinTS_cut15_12_42_good = TH1F('hist_ho_totfCinTS_cut15_12_42_good','hist_ho_totfCinTS_cut15_12_42_good',10,0,10)
hist_ho_totfCinTS_cut15_12_43_good = TH1F('hist_ho_totfCinTS_cut15_12_43_good','hist_ho_totfCinTS_cut15_12_43_good',10,0,10)
hist_ho_totfCinTS_cut15_12_41_bad  = TH1F('hist_ho_totfCinTS_cut15_12_41_bad', 'hist_ho_totfCinTS_cut15_12_41_bad',10,0,10)
hist_ho_totfCinTS_cut15_12_42_bad  = TH1F('hist_ho_totfCinTS_cut15_12_42_bad', 'hist_ho_totfCinTS_cut15_12_42_bad',10,0,10)
hist_ho_totfCinTS_cut15_12_43_bad  = TH1F('hist_ho_totfCinTS_cut15_12_43_bad', 'hist_ho_totfCinTS_cut15_12_43_bad',10,0,10)

#tight cuts: ho in each relevant channel
hist_ho_totADCinTS_cut20_12_40      = TH1F('hist_ho_totADCinTS_cut20_12_40',     'hist_ho_totADCinTS_cut20_12_40'     ,10,0,10)
hist_ho_totADCinTS_cut20_12_44      = TH1F('hist_ho_totADCinTS_cut20_12_44',     'hist_ho_totADCinTS_cut20_12_44'     ,10,0,10)
hist_ho_totADCinTS_cut20_12_41_good = TH1F('hist_ho_totADCinTS_cut20_12_41_good','hist_ho_totADCinTS_cut20_12_41_good',10,0,10)
hist_ho_totADCinTS_cut20_12_42_good = TH1F('hist_ho_totADCinTS_cut20_12_42_good','hist_ho_totADCinTS_cut20_12_42_good',10,0,10)
hist_ho_totADCinTS_cut20_12_43_good = TH1F('hist_ho_totADCinTS_cut20_12_43_good','hist_ho_totADCinTS_cut20_12_43_good',10,0,10)
hist_ho_totADCinTS_cut20_12_41_bad  = TH1F('hist_ho_totADCinTS_cut20_12_41_bad', 'hist_ho_totADCinTS_cut20_12_41_bad' ,10,0,10)
hist_ho_totADCinTS_cut20_12_42_bad  = TH1F('hist_ho_totADCinTS_cut20_12_42_bad', 'hist_ho_totADCinTS_cut20_12_42_bad' ,10,0,10)
hist_ho_totADCinTS_cut20_12_43_bad  = TH1F('hist_ho_totADCinTS_cut20_12_43_bad', 'hist_ho_totADCinTS_cut20_12_43_bad' ,10,0,10)

hist_ho_totfCinTS_cut20_12_40      = TH1F('hist_ho_totfCinTS_cut20_12_40',     'hist_ho_totfCinTS_cut20_12_40'     ,10,0,10)
hist_ho_totfCinTS_cut20_12_44      = TH1F('hist_ho_totfCinTS_cut20_12_44',     'hist_ho_totfCinTS_cut20_12_44'     ,10,0,10)
hist_ho_totfCinTS_cut20_12_41_good = TH1F('hist_ho_totfCinTS_cut20_12_41_good','hist_ho_totfCinTS_cut20_12_41_good',10,0,10)
hist_ho_totfCinTS_cut20_12_42_good = TH1F('hist_ho_totfCinTS_cut20_12_42_good','hist_ho_totfCinTS_cut20_12_42_good',10,0,10)
hist_ho_totfCinTS_cut20_12_43_good = TH1F('hist_ho_totfCinTS_cut20_12_43_good','hist_ho_totfCinTS_cut20_12_43_good',10,0,10)
hist_ho_totfCinTS_cut20_12_41_bad  = TH1F('hist_ho_totfCinTS_cut20_12_41_bad', 'hist_ho_totfCinTS_cut20_12_41_bad' ,10,0,10)
hist_ho_totfCinTS_cut20_12_42_bad  = TH1F('hist_ho_totfCinTS_cut20_12_42_bad', 'hist_ho_totfCinTS_cut20_12_42_bad' ,10,0,10)
hist_ho_totfCinTS_cut20_12_43_bad  = TH1F('hist_ho_totfCinTS_cut20_12_43_bad', 'hist_ho_totfCinTS_cut20_12_43_bad' ,10,0,10)

#how many adc counts/how much total charge in a 4TS sized pulse?
hist_ho_summedADC_soi0_12_414243_nocut_good = TH1F('hist_ho_summedADC_soi0_12_414243_nocut_good','hist_ho_summedADC_soi0_12_414243_nocut_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_nocut_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_nocut_bad' ,'hist_ho_summedADC_soi0_12_414243_nocut_bad' ,600,0,600)
hist_ho_summedADC_soi0_12_414243_cut15_good = TH1F('hist_ho_summedADC_soi0_12_414243_cut15_good','hist_ho_summedADC_soi0_12_414243_cut15_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_cut15_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_cut15_bad' ,'hist_ho_summedADC_soi0_12_414243_cut15_bad' ,600,0,600)
hist_ho_summedADC_soi0_12_414243_cut20_good = TH1F('hist_ho_summedADC_soi0_12_414243_cut20_good','hist_ho_summedADC_soi0_12_414243_cut20_good',600,0,600)
hist_ho_summedADC_soi0_12_414243_cut20_bad  = TH1F('hist_ho_summedADC_soi0_12_414243_cut20_bad' ,'hist_ho_summedADC_soi0_12_414243_cut20_bad' ,600,0,600)

hist_ho_summedADC_soi4_12_414243_nocut_good = TH1F('hist_ho_summedADC_soi4_12_414243_nocut_good','hist_ho_summedADC_soi4_12_414243_nocut_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_nocut_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_nocut_bad' ,'hist_ho_summedADC_soi4_12_414243_nocut_bad' ,600,0,600)
hist_ho_summedADC_soi4_12_414243_cut15_good = TH1F('hist_ho_summedADC_soi4_12_414243_cut15_good','hist_ho_summedADC_soi4_12_414243_cut15_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_cut15_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_cut15_bad' ,'hist_ho_summedADC_soi4_12_414243_cut15_bad' ,600,0,600)
hist_ho_summedADC_soi4_12_414243_cut20_good = TH1F('hist_ho_summedADC_soi4_12_414243_cut20_good','hist_ho_summedADC_soi4_12_414243_cut20_good',600,0,600)
hist_ho_summedADC_soi4_12_414243_cut20_bad  = TH1F('hist_ho_summedADC_soi4_12_414243_cut20_bad' ,'hist_ho_summedADC_soi4_12_414243_cut20_bad' ,600,0,600)

hist_ho_summedfC_soi0_12_414243_nocut_good = TH1F('hist_ho_summedfC_soi0_12_414243_nocut_good','hist_ho_summedfC_soi0_12_414243_nocut_good',6000,0,6000)
hist_ho_summedfC_soi0_12_414243_nocut_bad  = TH1F('hist_ho_summedfC_soi0_12_414243_nocut_bad' ,'hist_ho_summedfC_soi0_12_414243_nocut_bad' ,6000,0,6000)
hist_ho_summedfC_soi0_12_414243_cut15_good = TH1F('hist_ho_summedfC_soi0_12_414243_cut15_good','hist_ho_summedfC_soi0_12_414243_cut15_good',6000,0,6000)
hist_ho_summedfC_soi0_12_414243_cut15_bad  = TH1F('hist_ho_summedfC_soi0_12_414243_cut15_bad' ,'hist_ho_summedfC_soi0_12_414243_cut15_bad' ,6000,0,6000)
hist_ho_summedfC_soi0_12_414243_cut20_good = TH1F('hist_ho_summedfC_soi0_12_414243_cut20_good','hist_ho_summedfC_soi0_12_414243_cut20_good',6000,0,6000)
hist_ho_summedfC_soi0_12_414243_cut20_bad  = TH1F('hist_ho_summedfC_soi0_12_414243_cut20_bad' ,'hist_ho_summedfC_soi0_12_414243_cut20_bad' ,6000,0,6000)
                                                                                                                                                      
hist_ho_summedfC_soi4_12_414243_nocut_good = TH1F('hist_ho_summedfC_soi4_12_414243_nocut_good','hist_ho_summedfC_soi4_12_414243_nocut_good',6000,0,6000)
hist_ho_summedfC_soi4_12_414243_nocut_bad  = TH1F('hist_ho_summedfC_soi4_12_414243_nocut_bad' ,'hist_ho_summedfC_soi4_12_414243_nocut_bad' ,6000,0,6000)
hist_ho_summedfC_soi4_12_414243_cut15_good = TH1F('hist_ho_summedfC_soi4_12_414243_cut15_good','hist_ho_summedfC_soi4_12_414243_cut15_good',6000,0,6000)
hist_ho_summedfC_soi4_12_414243_cut15_bad  = TH1F('hist_ho_summedfC_soi4_12_414243_cut15_bad' ,'hist_ho_summedfC_soi4_12_414243_cut15_bad' ,6000,0,6000)
hist_ho_summedfC_soi4_12_414243_cut20_good = TH1F('hist_ho_summedfC_soi4_12_414243_cut20_good','hist_ho_summedfC_soi4_12_414243_cut20_good',6000,0,6000)
hist_ho_summedfC_soi4_12_414243_cut20_bad  = TH1F('hist_ho_summedfC_soi4_12_414243_cut20_bad' ,'hist_ho_summedfC_soi4_12_414243_cut20_bad' ,6000,0,6000)

# individual branches to get
b_bx = array('I', [0])
b_ls = array('I', [0])
chain.SetBranchAddress("bx", b_bx )
chain.SetBranchAddress("ls", b_ls )

chain.SetBranchStatus('*',0)
chain.SetBranchStatus("ls", 1 )
chain.SetBranchStatus("bx", 1 )
chain.SetBranchStatus("HODigiIEta", 1 )
chain.SetBranchStatus("HODigiIPhi", 1 )
chain.SetBranchStatus("HODigiCapID", 1 )
chain.SetBranchStatus("HODigiADC", 1 )
chain.SetBranchStatus("HODigiFC", 1 )
chain.SetBranchStatus("QIE11DigiADC", 1 )
chain.SetBranchStatus("QIE11DigiFC", 1 )
chain.SetBranchStatus("HBHEDigiADC", 1 )
chain.SetBranchStatus("HBHEDigiFC", 1 )

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
  ls = b_ls[0]
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
    sum_fc_soi0 = 0
    sum_fc_soi4 = 0
    eta = chain.HODigiIEta[i]
    phi = chain.HODigiIPhi[i]
    soicapid = chain.HODigiCapID[i][4]
    for j in range(ts_ho):
     adc.append(chain.HODigiADC[i][j])
     fc.append(chain.HODigiFC[i][j])
    
    if not ( (soicapid - bx) % 4 == 1 ) : bad_hit = True
    if max(adc)>20: tight = True
    if max(adc)>15: loose = True
      
    for j in range(ts_ho): #for every timeslice, fill plots
      if bad_hit: hist_ho_badhits_etaphi.Fill(eta, phi)

      if tight:
        if eta == 12:
          if phi == 40:
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_totADCinTS_cut20_12_40.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20_12_40.Fill(j, fc[j])

          elif phi == 41:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut20_12_41_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_41_bad.Fill(j, fc[j])
              if j==0: #only fill once per hit
                hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut20_12_41_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_41_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_good.Fill(sum_fc_soi0)

          elif phi == 42:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut20_12_42_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_42_bad.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut20_12_42_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_42_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_good.Fill(sum_fc_soi0)

          elif phi == 43:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut20_12_43_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_43_bad.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut20_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut20_12_43_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut20_12_43_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut20_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut20_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut20_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut20_good.Fill(sum_fc_soi0)

          elif phi == 44:
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])
            hist_ho_totADCinTS_cut20_12_44.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20_12_44.Fill(j, fc[j])

          else: #if eta12 but not one of our phis
            hist_ho_totADCinTS_cut20.Fill(j, adc[j])
            hist_ho_allADCinTS_cut20.Fill(j, adc[j])
            hist_ho_totfCinTS_cut20.Fill(j, fc[j])
            hist_ho_allfCinTS_cut20.Fill(j, fc[j])

        else: #if not eta12
          hist_ho_totADCinTS_cut20.Fill(j, adc[j])
          hist_ho_allADCinTS_cut20.Fill(j, adc[j])
          hist_ho_totfCinTS_cut20.Fill(j, fc[j])
          hist_ho_allfCinTS_cut20.Fill(j, fc[j])
    
      if loose:
        if eta == 12:
          if phi == 40:
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])
            hist_ho_totADCinTS_cut15_12_40.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15_12_40.Fill(j, fc[j])

          elif phi == 41:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut15_12_41_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_41_bad.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut15_12_41_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_41_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_good.Fill(sum_fc_soi0)

          elif phi == 42:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut15_12_42_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_42_bad.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut15_12_42_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_42_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_good.Fill(sum_fc_soi0)

          elif phi == 43:
            sum_adc_soi4 = sum(adc[2:6])
            sum_adc_soi0 = sum(adc[0:4])
            sum_fc_soi4 = sum(fc[2:6])
            sum_fc_soi0 = sum(fc[0:4])

            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])

            if bad_hit:
              hist_ho_totADCinTS_cut15_12_43_bad.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_43_bad.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_bad.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_bad.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_bad.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_bad.Fill(sum_fc_soi0)

            else:
              hist_ho_totADCinTS_cut15_12_43_good.Fill(j, adc[j])
              hist_ho_totfCinTS_cut15_12_43_good.Fill(j, fc[j])
              if j==0:
                hist_ho_summedADC_soi4_12_414243_cut15_good.Fill(sum_adc_soi4)
                hist_ho_summedADC_soi0_12_414243_cut15_good.Fill(sum_adc_soi0)
                hist_ho_summedfC_soi4_12_414243_cut15_good.Fill(sum_fc_soi4)
                hist_ho_summedfC_soi0_12_414243_cut15_good.Fill(sum_fc_soi0)

          elif phi == 44:
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])
            hist_ho_totADCinTS_cut15_12_44.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15_12_44.Fill(j, fc[j])

          else: #if eta12 but not one of our phis
            hist_ho_totADCinTS_cut15.Fill(j, adc[j])
            hist_ho_allADCinTS_cut15.Fill(j, adc[j])
            hist_ho_totfCinTS_cut15.Fill(j, fc[j])
            hist_ho_allfCinTS_cut15.Fill(j, fc[j])

        else: #if not eta12
          hist_ho_totADCinTS_cut15.Fill(j, adc[j])
          hist_ho_allADCinTS_cut15.Fill(j, adc[j])
          hist_ho_totfCinTS_cut15.Fill(j, fc[j])
          hist_ho_allfCinTS_cut15.Fill(j, fc[j])

      if eta == 12: #if not tight or loose
        if phi == 40:
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])
          hist_ho_totADCinTS_nocut_12_40.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut_12_40.Fill(j, fc[j])
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, fc[j])

        elif phi == 41:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          sum_fc_soi4 = sum(fc[2:6])
          sum_fc_soi0 = sum(fc[0:4])

          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])

          if j==0: #only fill this plot once for every hit
            hist_ho_numtotperls.Fill(ls)

          if bad_hit: #only fill this plot once for every hit
            hist_ho_totfCinTS_nocut_12_41_bad.Fill(j, fc[j])
            hist_ho_totADCinTS_nocut_12_41_bad.Fill(j, adc[j])
            if j==0:  #only fill this plot once for every hit
              hist_ho_numbadperls.Fill(ls)
              hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_bad.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_bad.Fill(sum_fc_soi0)

          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, fc[j])
            hist_ho_totADCinTS_nocut_12_41_good.Fill(j, adc[j])
            hist_ho_totfCinTS_nocut_12_41_good.Fill(j, fc[j])
            if j==0:  #only fill this plot once for every hit
              hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_good.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_good.Fill(sum_fc_soi0)

        elif phi == 42:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          sum_fc_soi4 = sum(fc[2:6])
          sum_fc_soi0 = sum(fc[0:4])

          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])

          if j==0: 
            hist_ho_numtotperls.Fill(ls)

          if bad_hit:
            hist_ho_totfCinTS_nocut_12_42_bad.Fill(j, fc[j])
            hist_ho_totADCinTS_nocut_12_42_bad.Fill(j, adc[j])
            if j==0: 
              hist_ho_numbadperls.Fill(ls)
              hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_bad.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_bad.Fill(sum_fc_soi0)

          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, fc[j])
            hist_ho_totADCinTS_nocut_12_42_good.Fill(j, adc[j])
            hist_ho_totfCinTS_nocut_12_42_good.Fill(j, fc[j])
            if j==0: 
              hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_good.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_good.Fill(sum_fc_soi0)

        elif phi == 43:
          sum_adc_soi4 = sum(adc[2:6])
          sum_adc_soi0 = sum(adc[0:4])
          sum_fc_soi4 = sum(fc[2:6])
          sum_fc_soi0 = sum(fc[0:4])

          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])

          if j==0: 
            hist_ho_numtotperls.Fill(ls)

          if bad_hit:
            hist_ho_totADCinTS_nocut_12_43_bad.Fill(j, adc[j])
            hist_ho_totfCinTS_nocut_12_43_bad.Fill(j, fc[j])
            if j==0: 
              hist_ho_numbadperls.Fill(ls)
              hist_ho_summedADC_soi4_12_414243_nocut_bad.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_bad.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_bad.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_bad.Fill(sum_fc_soi0)

          else:
            hist_ho_totADCinTS_allgood.Fill(j, adc[j])
            hist_ho_totfCinTS_allgood.Fill(j, fc[j])
            hist_ho_totADCinTS_nocut_12_43_good.Fill(j, adc[j])
            hist_ho_totfCinTS_nocut_12_43_good.Fill(j, fc[j])
            if j==0: 
              hist_ho_summedADC_soi4_12_414243_nocut_good.Fill(sum_adc_soi4)
              hist_ho_summedADC_soi0_12_414243_nocut_good.Fill(sum_adc_soi0)
              hist_ho_summedfC_soi4_12_414243_nocut_good.Fill(sum_fc_soi4)
              hist_ho_summedfC_soi0_12_414243_nocut_good.Fill(sum_fc_soi0)

        elif phi == 44:
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, fc[j])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])
          hist_ho_totADCinTS_nocut_12_44.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut_12_44.Fill(j, fc[j])

        else: #if eta12 but not one of our phis
          hist_ho_totADCinTS_allgood.Fill(j, adc[j])
          hist_ho_totfCinTS_allgood.Fill(j, fc[j])
          hist_ho_totADCinTS_nocut.Fill(j, adc[j])
          hist_ho_allADCinTS_nocut.Fill(j, adc[j])
          hist_ho_totfCinTS_nocut.Fill(j, fc[j])
          hist_ho_allfCinTS_nocut.Fill(j, fc[j])

      else: #if not eta12
        hist_ho_totADCinTS_allgood.Fill(j, adc[j])
        hist_ho_totfCinTS_allgood.Fill(j, fc[j])
        hist_ho_totADCinTS_nocut.Fill(j, adc[j])
        hist_ho_allADCinTS_nocut.Fill(j, adc[j])
        hist_ho_totfCinTS_nocut.Fill(j, fc[j])
        hist_ho_allfCinTS_nocut.Fill(j, fc[j])

  # HE PLOTS
  for i in range(hits_he): #for every he hit in the event:  
    adc=[]
    fc=[]
    tight = False
    loose = False
    for j in range(ts_he):
     adc.append(chain.QIE11DigiADC[i][j])
     fc.append(chain.QIE11DigiFC[i][j])

    if max(adc)>15: tight = True
    if max(adc)>10: loose = True

    for j in range(ts_he):
      if tight:
        hist_he_totADCinTS_cut15.Fill(j, adc[j])
        hist_he_allADCinTS_cut15.Fill(j, adc[j])
        hist_he_totfCinTS_cut15.Fill(j, fc[j])
        hist_he_allfCinTS_cut15.Fill(j, fc[j])

      if loose:
        hist_he_totADCinTS_cut10.Fill(j, adc[j])
        hist_he_allADCinTS_cut10.Fill(j, adc[j])
        hist_he_totfCinTS_cut10.Fill(j, fc[j])
        hist_he_allfCinTS_cut10.Fill(j, fc[j])

      hist_he_totADCinTS_nocut.Fill(j, adc[j])
      hist_he_allADCinTS_nocut.Fill(j, adc[j])
      hist_he_totfCinTS_nocut.Fill(j, fc[j])
      hist_he_allfCinTS_nocut.Fill(j, fc[j])

  # HB PLOTS
  for i in range(hits_hb): #for every he hit in the event:  
    adc=[]
    fc=[]
    tight = False
    loose = False
    for j in range(ts_hb):
     adc.append(chain.HBHEDigiADC[i][j])
     fc.append(chain.HBHEDigiFC[i][j])

    if max(adc)>8: tight = True
    if max(adc)>5: loose = True

    for j in range(ts_hb):
      if tight:
        hist_hb_totADCinTS_cut8.Fill(j, adc[j])
        hist_hb_allADCinTS_cut8.Fill(j, adc[j])
        hist_hb_totfCinTS_cut8.Fill(j, fc[j])
        hist_hb_allfCinTS_cut8.Fill(j, fc[j])

      if loose:
        hist_hb_totADCinTS_cut5.Fill(j, adc[j])
        hist_hb_allADCinTS_cut5.Fill(j, adc[j])
        hist_hb_totfCinTS_cut5.Fill(j, fc[j])
        hist_hb_allfCinTS_cut5.Fill(j, fc[j])

      hist_hb_totADCinTS_nocut.Fill(j, adc[j])
      hist_hb_allADCinTS_nocut.Fill(j, adc[j])
      hist_hb_totfCinTS_nocut.Fill(j, fc[j])
      hist_hb_allfCinTS_nocut.Fill(j, fc[j])

  count += 1
#  if count == 50: break

# Save file
out_file.cd()
out_file.Write()
out_file.Close()

print('Time elapsed: %.1f' % (time.time() - time_begin), 'sec')
