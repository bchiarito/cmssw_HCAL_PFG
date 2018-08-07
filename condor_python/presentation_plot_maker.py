from ROOT import *
import sys

CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900
#gStyle.SetOptStat(110000)
#gStyle.SetOptStat(0)

# setup
fi = TFile(sys.argv[1])
run = sys.argv[2]
run_string = ''
run_num = '_run_'+str(run)
w = CANVAS_WIDTH
h = CANVAS_HEIGHT
c = TCanvas('c','c',w,h)
#c = TCanvas('c','c')

# FED vs LS plots
badhits_title = 'Run '+run+": "+"Number of bad hits"
fractionbad_title = 'Run '+run+": "+"Fraction of bad hits"
FED_low = 724
FED_high = 731
LS_low = 0
LS_high = 0
if run == 316110: LS_high = 209
if run == 316972: LS_high = 44
if run == 318974: LS_high = 106
if run == 319629: LS_high = 57
if run == 320062: LS_high = 31

numer = fi.Get("hist_FEDvsLS_bad")
denom = fi.Get("hist_FEDvsLS_total")
fraction = numer.Clone()
fraction.Divide(denom)
numer.SetTitle(badhits_title)
fraction.SetTitle(fractionbad_title)

numer.Draw('Colz')
#numer.GetXaxis().SetLimits(LS_low, LS_high)
#numer.GetYaxis().SetLimits(FED_low, FED_high)
c.Update()
c.SaveAs(run_string+"FEDvsLS_badhits"+run_num+".png")
c.SaveAs(run_string+"FEDvsLS_badhits"+run_num+".root")
fraction.Draw('Colz')
#fraction.GetXaxis().SetLimits(LS_low, LS_high)
#fraction.GetYaxis().SetLimits(FED_low, FED_high)
c.Update()
c.SaveAs(run_string+"FEDvsLS_fractionbad"+run_num+".png")
c.SaveAs(run_string+"FEDvsLS_fractionbad"+run_num+".root")

# heat maps plots
xaxis = 'iEta'
yaxis = 'iPhi'
title_good = 'Run '+run+': '+'Heat map of good hits'
title_bad = 'Run '+run+': '+'Heat map of bad hits'

good_hits = fi.Get('hist_goodhits_etaphi')
bad_hits = fi.Get('hist_badhits_etaphi')
good_hits.SetTitle(title_good)
good_hits.GetXaxis().SetTitle(xaxis)
good_hits.GetYaxis().SetTitle(yaxis)
bad_hits.SetTitle(title_bad)
bad_hits.GetXaxis().SetTitle(xaxis)
bad_hits.GetYaxis().SetTitle(yaxis)

good_hits.Draw('Colz')
c.SaveAs("heatmap_goodhits"+run_num+".png")
c.SaveAs("heatmap_goodhits"+run_num+".root")
bad_hits.Draw('Colz')
c.SaveAs("heatmap_badhits"+run_num+".png")
c.SaveAs("heatmap_badhits"+run_num+".root")

# Steffie's TS vs charge plots
xaxis = 'highest charge TS'
yaxis = 'fC'
title_good = 'Run '+run+': '+'TS with highest charge vs fC in that TS, good hits'
title_bad = 'Run '+run+': '+'TS with highest charge vs fC in that TS, bad hits'

bad_hits = fi.Get('hist_TSvsfC_highest_bad')
good_hits = fi.Get('hist_TSvsfC_highest_good')

good_hits.SetTitle(title_good)
good_hits.GetXaxis().SetTitle(xaxis)
good_hits.GetYaxis().SetTitle(yaxis)
bad_hits.SetTitle(title_bad)
bad_hits.GetXaxis().SetTitle(xaxis)
bad_hits.GetYaxis().SetTitle(yaxis)

good_hits.Draw('Colz')
c.SaveAs("highest_ts_vs_fc_good"+run_num+".png")
c.SaveAs("highest_ts_vs_fc_good"+run_num+".root")
bad_hits.Draw('Colz')
c.SaveAs("highest_ts_vs_fc_bad"+run_num+".png")
c.SaveAs("highest_ts_vs_fc_bad"+run_num+".root")

# capid-bx mod 4 plots
xaxis = "(CapID - BX) % 4"
yaxis = "Hits"

ho_title = 'Run '+run+": "+"HO"
he_title = 'Run '+run+": "+"HE"
hf_title = 'Run '+run+": "+"HF"
hb_title = 'Run '+run+": "+"HB"

ho = fi.Get("hist_capcheck_ho")
he = fi.Get("hist_capcheck_he")
hf = fi.Get("hist_capcheck_hf")
hb = fi.Get("hist_capcheck_hb")
ho.SetTitle(ho_title)
he.SetTitle(he_title)
hf.SetTitle(hf_title)
hb.SetTitle(hb_title)
capid_bx_hists = []
capid_bx_hists.append(ho)
capid_bx_hists.append(he)
capid_bx_hists.append(hf)
capid_bx_hists.append(hb)
for hist in capid_bx_hists:
  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)

c.SetLogy(1)
ho.Draw()
c.SaveAs(run_string+"capid_bx_mod4_ho"+run_num+".png")
c.SaveAs(run_string+"capid_bx_mod4_ho"+run_num+".root")
he.Draw()
c.SaveAs(run_string+"capid_bx_mod4_he"+run_num+".png")
c.SaveAs(run_string+"capid_bx_mod4_he"+run_num+".root")
hf.Draw()
c.SaveAs(run_string+"capid_bx_mod4_hf"+run_num+".png")
c.SaveAs(run_string+"capid_bx_mod4_hf"+run_num+".root")
hb.Draw()
c.SaveAs(run_string+"capid_bx_mod4_hb"+run_num+".png")
c.SaveAs(run_string+"capid_bx_mod4_hb"+run_num+".root")
c.SetLogy(0)

# First capID plots
xaxis = "CapID of TS 0"
yaxis = "Hits"
ho_title = 'Run '+run+": "+"CapID of TS 0 for hits in HO"
he_title = 'Run '+run+": "+"CapID of TS 0 for hits in HE"
hf_title = 'Run '+run+": "+"CapID of TS 0 for hits in HF"
hb_title = 'Run '+run+": "+"CapID of TS 0 for hits in HB"
low = 0

ho = fi.Get("hist_firstID_ho")
he = fi.Get("hist_firstID_he")
hf = fi.Get("hist_firstID_hf")
hb = fi.Get("hist_firstID_hb")
ho.SetTitle(ho_title)
he.SetTitle(he_title)
hf.SetTitle(hf_title)
hb.SetTitle(hb_title)
firstcapid_hists = []
firstcapid_hists.append(ho)
firstcapid_hists.append(he)
firstcapid_hists.append(hf)
firstcapid_hists.append(hb)
for hist in firstcapid_hists:
  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)
  hist.SetMinimum(low)

ho.Draw()
c.SaveAs(run_string+"first_capid_ho"+run_num+".png")
c.SaveAs(run_string+"first_capid_ho"+run_num+".root")
he.Draw()
c.SaveAs(run_string+"first_capid_he"+run_num+".png")
c.SaveAs(run_string+"first_capid_he"+run_num+".root")
hf.Draw()
c.SaveAs(run_string+"first_capid_hf"+run_num+".png")
c.SaveAs(run_string+"first_capid_hf"+run_num+".root")
hb.Draw()
c.SaveAs(run_string+"first_capid_hb"+run_num+".png")
c.SaveAs(run_string+"first_capid_hb"+run_num+".root")

# average charge per TS plots
xaxis = "TS"
yaxis = 'Average Charge (fC)'
title = 'Run '+run+": "+"Average Charge per Time Slice"
good_color = kBlack
bad_color = kRed
legend_title = ''
legend_xi = 0.7
legend_xf = 0.9
legend_yi = 0.7
legend_yf = 0.8
legend_good_label = 'Good hits'
legend_bad_label = 'Bad hits'
low = 0
high = 25

ho_good = fi.Get("hist_avgfCvsTS_ho_good")
ho_bad = fi.Get("hist_avgfCvsTS_ho_bad")
ho_good.GetXaxis().SetTitle(xaxis)
ho_good.GetYaxis().SetTitle(yaxis)
ho_good.SetTitle(title)
ho_bad.GetXaxis().SetTitle(xaxis)
ho_bad.GetYaxis().SetTitle(yaxis)
ho_bad.SetTitle(title)
ho_good.SetLineColor(good_color)
ho_bad.SetLineColor(bad_color)
leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
leg.AddEntry(ho_good, legend_good_label, 'l')
leg.AddEntry(ho_bad, legend_bad_label, 'l')
ho_bad.SetMinimum(low)
ho_good.SetMinimum(low)

ho_bad.Draw()
ho_good.Draw('same')
leg.Draw('same')
c.SaveAs(run_string+"avgfC_per_TS"+run_num+".png")
c.SaveAs(run_string+"avgfC_per_TS"+run_num+".root")

# average charge per TS compare cut vs nocut plots
xaxis = "TS"
#yaxis = 'Average charge (fC)'
yaxis = 'Scaled to Integral 100'
title = 'Run '+run+": "+"Average charge per TS, good hits"
wcut_color = kBlue
wocut_color = kBlack
legend_title = ''
legend_xi = 0.7
legend_xf = 0.9
legend_yi = 0.7
legend_yf = 0.8
legend_wcut_label = 'Exclude fC < 1'
legend_wocut_label = 'Include fC > 1'

ho_wcut = fi.Get("hist_avgfCvsTS_cut_ho_good")
#ho_wcut.Scale(10.0 / ho_wcut.GetEntries())
ho_wocut = fi.Get("hist_avgfCvsTS_ho_good")
ho_wcut.GetXaxis().SetTitle(xaxis)
ho_wcut.GetYaxis().SetTitle(yaxis)
ho_wcut.SetTitle(title)
ho_wocut.GetXaxis().SetTitle(xaxis)
ho_wocut.GetYaxis().SetTitle(yaxis)
ho_wocut.SetTitle(title)
ho_wcut.SetLineColor(wcut_color)
ho_wocut.SetLineColor(wocut_color)
leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
leg.AddEntry(ho_wcut, legend_wcut_label, 'l')
leg.AddEntry(ho_wocut, legend_wocut_label, 'l')
ho_wocut.Scale(100.0 / ho_wocut.Integral())
ho_wcut.Scale(100.0 / ho_wcut.Integral())

ho_wocut.Draw()
ho_wcut.Draw('same')
leg.Draw('same')
c.SaveAs(run_string+"avgfC_per_TS_compare_1fC_cut"+run_num+".png")
c.SaveAs(run_string+"avgfC_per_TS_compare_1fC_cut"+run_num+".root")

# total pulse charge plots
xaxis = 'fC'
yaxis = 'Scaled to integral 100'
soi0_title = 'Run '+run+": "+'Total charge in TS 0->3'
soi4_title = 'Run '+run+": "+'Total charge in TS 2->5'
good_color = kBlack
bad_color = kRed
legend_title = ''
legend_xi = 0.7
legend_xf = 0.9
legend_yi = 0.7
legend_yf = 0.8
legend_good_label = 'Good hits'
legend_bad_label = 'Bad hits'
low = 0
high = 12

ho_soi0_good = fi.Get("hist_totalfC_ho_soi0_good")
ho_soi0_bad = fi.Get("hist_totalfC_ho_soi0_bad")
ho_soi0_good.GetXaxis().SetTitle(xaxis)
ho_soi0_good.GetYaxis().SetTitle(yaxis)
ho_soi0_good.SetTitle(soi0_title)
ho_soi0_good.SetLineColor(good_color)
ho_soi0_bad.GetXaxis().SetTitle(xaxis)
ho_soi0_bad.GetYaxis().SetTitle(yaxis)
ho_soi0_bad.SetTitle(soi0_title)
ho_soi0_bad.SetLineColor(bad_color)
leg_soi0 = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
leg_soi0.AddEntry(ho_soi0_good, legend_good_label, 'l')
leg_soi0.AddEntry(ho_soi0_bad, legend_bad_label, 'l')
ho_soi4_good = fi.Get("hist_totalfC_ho_soi4_good")
ho_soi4_bad = fi.Get("hist_totalfC_ho_soi4_bad")
ho_soi4_good.GetXaxis().SetTitle(xaxis)
ho_soi4_good.GetYaxis().SetTitle(yaxis)
ho_soi4_good.SetTitle(soi4_title)
ho_soi4_good.SetLineColor(good_color)
ho_soi4_bad.GetXaxis().SetTitle(xaxis)
ho_soi4_bad.GetYaxis().SetTitle(yaxis)
ho_soi4_bad.SetTitle(soi4_title)
ho_soi4_bad.SetLineColor(bad_color)
leg_soi4 = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
leg_soi4.AddEntry(ho_soi4_good, legend_good_label, 'l')
leg_soi4.AddEntry(ho_soi4_bad, legend_bad_label, 'l')
ho_soi0_good.Scale(100.0/ho_soi0_good.Integral())
ho_soi0_bad.Scale(100.0/ho_soi0_bad.Integral())
ho_soi4_good.Scale(100.0/ho_soi4_good.Integral())
ho_soi4_bad.Scale(100.0/ho_soi4_bad.Integral())
ho_soi0_good.SetMinimum(low)
ho_soi0_good.SetMaximum(high)
ho_soi0_bad.SetMinimum(low)
ho_soi0_bad.SetMaximum(high)
ho_soi4_good.SetMinimum(low)
ho_soi4_good.SetMaximum(high)
ho_soi4_bad.SetMinimum(low)
ho_soi4_bad.SetMaximum(high)

ho_soi0_bad.Draw('hist')
ho_soi0_good.Draw('hist same')
leg_soi0.Draw('same')
c.SaveAs(run_string+"total_pulse_charge_soi0"+run_num+".png")
c.SaveAs(run_string+"total_pulse_charge_soi0"+run_num+".root")

ho_soi4_bad.Draw('hist')
ho_soi4_good.Draw('hist same')
leg_soi4.Draw('same')
c.SaveAs(run_string+"total_pulse_charge_soi4"+run_num+".png")
c.SaveAs(run_string+"total_pulse_charge_soi4"+run_num+".root")

# total charge all pulses included
xaxis = 'fC'
yaxis = 'Scaled to integral 100'
title = 'Run '+run+": "+'Total charge in TS'
legend_title = ''
legend_xi = 0.8
legend_xf = 0.9
legend_yi = 0.5
legend_yf = 0.8
legend_ts0_label = 'TS 0'
legend_ts1_label = 'TS 1'
legend_ts2_label = 'TS 2'
legend_ts3_label = 'TS 3'
legend_ts4_label = 'TS 4'
legend_ts5_label = 'TS 5'
legend_ts6_label = 'TS 6'
legend_ts7_label = 'TS 7'
legend_ts8_label = 'TS 8'
legend_ts9_label = 'TS 9'
low = 0
high = 700000

ts0 = fi.Get("hist_totalfC_ho_TS0")
ts1 = fi.Get("hist_totalfC_ho_TS1")
ts2 = fi.Get("hist_totalfC_ho_TS2")
ts3 = fi.Get("hist_totalfC_ho_TS3")
ts4 = fi.Get("hist_totalfC_ho_TS4")
ts5 = fi.Get("hist_totalfC_ho_TS5")
ts6 = fi.Get("hist_totalfC_ho_TS6")
ts7 = fi.Get("hist_totalfC_ho_TS7")
ts8 = fi.Get("hist_totalfC_ho_TS8")
ts9 = fi.Get("hist_totalfC_ho_TS9")
ts_hists = []
ts_hists.append(ts0)
ts_hists.append(ts1)
ts_hists.append(ts2)
ts_hists.append(ts3)
ts_hists.append(ts4)
ts_hists.append(ts5)
ts_hists.append(ts6)
ts_hists.append(ts7)
ts_hists.append(ts8)
ts_hists.append(ts9)
for hist in ts_hists:
  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)
  hist.SetTitle(title)
  if not hist.Integral() == 0: hist.Scale( 100.0 / hist.Integral() )

ts0.SetLineColor(92)
ts1.SetLineColor(94)
ts2.SetLineColor(96)
ts3.SetLineColor(99)
ts4.SetLineColor(2)
ts5.SetLineColor(52)
ts6.SetLineColor(54)
ts7.SetLineColor(56)
ts8.SetLineColor(58)
ts9.SetLineColor(60)

leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
leg.AddEntry(ts0, legend_ts0_label, 'l')
leg.AddEntry(ts1, legend_ts1_label, 'l')
leg.AddEntry(ts2, legend_ts2_label, 'l')
leg.AddEntry(ts3, legend_ts3_label, 'l')
leg.AddEntry(ts4, legend_ts4_label, 'l')
leg.AddEntry(ts5, legend_ts5_label, 'l')
leg.AddEntry(ts6, legend_ts6_label, 'l')
leg.AddEntry(ts7, legend_ts7_label, 'l')
leg.AddEntry(ts8, legend_ts8_label, 'l')
leg.AddEntry(ts9, legend_ts9_label, 'l')

ts9.SetMinimum(low)

ts0.Draw('hist')
ts9.Draw('hist same')
ts1.Draw('hist same')
ts2.Draw('hist same')
ts3.Draw('hist same')
ts4.Draw('hist same')
ts5.Draw('hist same')
ts6.Draw('hist same')
ts7.Draw('hist same')
ts8.Draw('hist same')
leg.Draw('hist same')
c.SaveAs(run_string+"pulse_all_TS_separate"+run_num+".png")
c.SaveAs(run_string+"pulse_all_TS_separate"+run_num+".root")

