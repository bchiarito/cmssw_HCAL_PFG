from ROOT import *
import sys

CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900
#gStyle.SetOptStat(110000)
gStyle.SetOptStat(0)

# setup
fi = TFile(sys.argv[1])
run = sys.argv[2]
run_num = '_run_'+str(run)
run_string = 'Run '+run+': '
w = CANVAS_WIDTH
h = CANVAS_HEIGHT
c = TCanvas('c','c',w,h)
#c = TCanvas('c','c')
LS_low = 1
LS_high = 0
if run == 316110: LS_high = 209
if run == 316972: LS_high = 44
if run == 318974: LS_high = 106
if run == 319629: LS_high = 57
if run == 320062: LS_high = 31
if run == '321005 JetHT': LS_high = 59
if run == '321005': LS_high = 59

outputfile = TFile('histos'+run_num+'.root', 'RECREATE')

# 41, 42, 43 only
#if True:
if False:
  xaxis = 'TS'
  yaxis_ADC = 'ADC'
  yaxis_fC = 'fC'

  cut0_ADC_low = 8.5
  cut0_ADC_high = 11
  cut1_ADC_low = 8.5
  cut1_ADC_high = 11
  cut2_ADC_low = 8.5
  cut2_ADC_high = 16

  cut0_fC_low = 0
  cut0_fC_high = 6
  cut1_fC_low = 0
  cut1_fC_high = 6
  cut2_fC_low = 0
  cut2_fC_high = 30

  ho_title_ADC = 'HO, average ADC in bad channels only'
  ho_title_fC = 'HO, average fC in bad channels only'
  ho_cut0_title_ADC = run_string+ho_title_ADC+''
  ho_cut1_title_ADC = run_string+ho_title_ADC+', at least one pulse > ADC 15'
  ho_cut2_title_ADC = run_string+ho_title_ADC+', at least one pulse > ADC 20'
  ho_cut0_title_fC = run_string+ho_title_fC+''
  ho_cut1_title_fC = run_string+ho_title_fC+', at least one pulse > ADC 15'
  ho_cut2_title_fC = run_string+ho_title_fC+', at least one pulse > 20'

  color_40 = kBlue
  color_44 = kBlue
  color_41_good = kBlack
  color_41_bad = kRed
  color_42_good = kBlack
  color_42_bad = kRed
  color_43_good = kBlack
  color_43_bad = kRed

  legend_title = ''
  legend_xi = 0.75
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.9
  legend_40_label = 'iEta 12, iPhi 40'
  legend_44_label = 'iEta 12, iPhi 44'
  legend_41_good_label = 'iEta 12, iPhi 41, good hits'
  legend_41_bad_label = 'iEta 12, iPhi 41, bad hits'
  legend_42_good_label = 'iEta 12, iPhi 42, good hits'
  legend_42_bad_label = 'iEta 12, iPhi 42, bad hits'
  legend_43_good_label = 'iEta 12, iPhi 43, good hits'
  legend_43_bad_label = 'iEta 12, iPhi 43. bad hits'

  ho_cut0_ADC_41_good = fi.Get('hist_ho_totADCinTS_nocut_12_41_good')
  ho_cut0_ADC_41_bad = fi.Get('hist_ho_totADCinTS_nocut_12_41_bad')
  ho_cut0_ADC_42_good = fi.Get('hist_ho_totADCinTS_nocut_12_42_good')
  ho_cut0_ADC_42_bad = fi.Get('hist_ho_totADCinTS_nocut_12_42_bad')
  ho_cut0_ADC_43_good = fi.Get('hist_ho_totADCinTS_nocut_12_43_good')
  ho_cut0_ADC_43_bad = fi.Get('hist_ho_totADCinTS_nocut_12_43_bad')
  ho_cut0_ADC_41_good.SetLineColor(color_41_good)
  ho_cut0_ADC_41_bad.SetLineColor(color_41_bad)
  ho_cut0_ADC_42_good.SetLineColor(color_42_good)
  ho_cut0_ADC_42_bad.SetLineColor(color_42_bad)
  ho_cut0_ADC_43_good.SetLineColor(color_43_good)
  ho_cut0_ADC_43_bad.SetLineColor(color_43_bad)
  ho_cut0_ADC_41_good.Scale(10.0 / ho_cut0_ADC_41_good.GetEntries() )
  ho_cut0_ADC_41_bad.Scale(10.0 / ho_cut0_ADC_41_bad.GetEntries() )
  ho_cut0_ADC_42_good.Scale(10.0 / ho_cut0_ADC_42_good.GetEntries() )
  ho_cut0_ADC_42_bad.Scale(10.0 / ho_cut0_ADC_42_bad.GetEntries() )
  ho_cut0_ADC_43_good.Scale(10.0 / ho_cut0_ADC_43_good.GetEntries() )
  ho_cut0_ADC_43_bad.Scale(10.0 / ho_cut0_ADC_43_bad.GetEntries() )

  ho_cut0_fC_41_good = fi.Get('hist_ho_totfCinTS_nocut_12_41_good')
  ho_cut0_fC_41_bad = fi.Get('hist_ho_totfCinTS_nocut_12_41_bad')
  ho_cut0_fC_42_good = fi.Get('hist_ho_totfCinTS_nocut_12_42_good')
  ho_cut0_fC_42_bad = fi.Get('hist_ho_totfCinTS_nocut_12_42_bad')
  ho_cut0_fC_43_good = fi.Get('hist_ho_totfCinTS_nocut_12_43_good')
  ho_cut0_fC_43_bad = fi.Get('hist_ho_totfCinTS_nocut_12_43_bad')
  ho_cut0_fC_41_good.SetLineColor(color_41_good)
  ho_cut0_fC_41_bad.SetLineColor(color_41_bad)
  ho_cut0_fC_42_good.SetLineColor(color_42_good)
  ho_cut0_fC_42_bad.SetLineColor(color_42_bad)
  ho_cut0_fC_43_good.SetLineColor(color_43_good)
  ho_cut0_fC_43_bad.SetLineColor(color_43_bad)
  ho_cut0_fC_41_good.Scale(10.0 / ho_cut0_fC_41_good.GetEntries() )
  ho_cut0_fC_41_bad.Scale(10.0 / ho_cut0_fC_41_bad.GetEntries() )
  ho_cut0_fC_42_good.Scale(10.0 / ho_cut0_fC_42_good.GetEntries() )
  ho_cut0_fC_42_bad.Scale(10.0 / ho_cut0_fC_42_bad.GetEntries() )
  ho_cut0_fC_43_good.Scale(10.0 / ho_cut0_fC_43_good.GetEntries() )
  ho_cut0_fC_43_bad.Scale(10.0 / ho_cut0_fC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_ADC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_41_bad, legend_41_bad_label, 'l')
  ho_cut0_ADC_41_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC_41_good.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC_41_good.SetTitle(ho_cut0_title_ADC)
  ho_cut0_ADC_41_good.SetMaximum(cut0_ADC_high)
  ho_cut0_ADC_41_good.SetMinimum(cut0_ADC_low)
  ho_cut0_ADC_41_good.Draw()
  ho_cut0_ADC_41_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgADC_41only_compare_cut0'+run_num+'.png')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_ADC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_42_bad, legend_42_bad_label, 'l')
  ho_cut0_ADC_42_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC_42_good.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC_42_good.SetTitle(ho_cut0_title_ADC)
  ho_cut0_ADC_42_good.SetMaximum(cut0_ADC_high)
  ho_cut0_ADC_42_good.SetMinimum(cut0_ADC_low)
  ho_cut0_ADC_42_good.Draw()
  ho_cut0_ADC_42_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgADC_42only_compare_cut0'+run_num+'.png')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_ADC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_43_bad, legend_43_bad_label, 'l')
  ho_cut0_ADC_43_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC_43_good.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC_43_good.SetTitle(ho_cut0_title_ADC)
  ho_cut0_ADC_43_good.SetMaximum(cut0_ADC_high)
  ho_cut0_ADC_43_good.SetMinimum(cut0_ADC_low)
  ho_cut0_ADC_43_good.Draw()
  ho_cut0_ADC_43_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgADC_43only_compare_cut0'+run_num+'.png')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_fC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_41_bad, legend_41_bad_label, 'l')
  ho_cut0_fC_41_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC_41_good.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC_41_good.SetTitle(ho_cut0_title_fC)
  ho_cut0_fC_41_good.SetMaximum(cut0_fC_high)
  ho_cut0_fC_41_good.SetMinimum(cut0_fC_low)
  ho_cut0_fC_41_good.Draw()
  ho_cut0_fC_41_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgfC_41only_compare_cut0'+run_num+'.png')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_fC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_42_bad, legend_42_bad_label, 'l')
  ho_cut0_fC_42_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC_42_good.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC_42_good.SetTitle(ho_cut0_title_fC)
  ho_cut0_fC_42_good.SetMaximum(cut0_fC_high)
  ho_cut0_fC_42_good.SetMinimum(cut0_fC_low)
  ho_cut0_fC_42_good.Draw()
  ho_cut0_fC_42_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgfC_42only_compare_cut0'+run_num+'.png')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_fC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_43_bad, legend_43_bad_label, 'l')
  ho_cut0_fC_43_good.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC_43_good.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC_43_good.SetTitle(ho_cut0_title_fC)
  ho_cut0_fC_43_good.SetMaximum(cut0_fC_high)
  ho_cut0_fC_43_good.SetMinimum(cut0_fC_low)
  ho_cut0_fC_43_good.Draw()
  ho_cut0_fC_43_bad.Draw('same')
  leg.Draw('same')
  c.SaveAs('avgfC_43only_compare_cut0'+run_num+'.png')

# total pulse
if True:
#if False:
  xaxis_ADC = 'Summed total ADC'
  xaxis_fC = 'Summed total fC'
  yaxis = 'Scaled to unit integral'

  title_soi0_ADC_cut0 = run_string+'HO, ADC summed in TS 0-3'
  title_soi0_ADC_cut1 = run_string+'HO, ADC summed in TS 0-3, cut at 1'
  title_soi0_ADC_cut2 = run_string+'HO, ADC summed in TS 0-3, cut at 2'

  title_soi4_ADC_cut0 = run_string+'HO, ADC summed in TS 2-5'
  title_soi4_ADC_cut1 = run_string+'HO, ADC summed in TS 2-5, cut at 1'
  title_soi4_ADC_cut2 = run_string+'HO, ADC summed in TS 2-5, cut at 2'

  title_soi0_fC_cut0 = run_string+'HO, fC summed in TS 0-3'
  title_soi0_fC_cut1 = run_string+'HO, fC summed in TS 0-3, cut at 1'
  title_soi0_fC_cut2 = run_string+'HO, fC summed in TS 0-3, cut at 2'

  title_soi4_fC_cut0 = run_string+'HO, fC summed in TS 2-5'
  title_soi4_fC_cut1 = run_string+'HO, fC summed in TS 2-5, cut at 1'
  title_soi4_fC_cut2 = run_string+'HO, fC summed in TS 2-5, cut at 2'

  legend_title = ''
  legend_xi = 0.75
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.9
  good_label = 'Good hits'
  bad_label = 'Bad hits'
  good_color = kBlack
  bad_color = kRed

  ADC_low = 0
  ADC_high = 200
  ADC_veryhigh = 200
  fC_low = 0
  fC_high = 100
  fC_veryhigh = 200

  rebin = 4

  low = 10e-5
  c.SetLogy()

  # good = fi.Get('hist_ho_summedADC_soi0_12_414243_nocut_good')
  # bad = fi.Get('hist_ho_summedADC_soi0_12_414243_nocut_bad')
  # good.GetXaxis().SetTitle(xaxis_ADC)
  # good.GetYaxis().SetTitle(yaxis)
  # good.SetTitle(title_soi0_ADC_cut0)
  # good.GetXaxis().SetRange(1, good.GetBin(ADC_high))
  # bad.GetXaxis().SetRange(1, bad.GetBin(ADC_high))
  # good.Scale(1.0 / good.Integral())
  # bad.Scale(1.0 / bad.Integral())
  # good.SetMinimum(low)
  # good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  # good.SetLineColor(good_color)
  # bad.SetLineColor(bad_color)
  # leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  # leg.AddEntry(good, good_label, 'l')
  # leg.AddEntry(bad, bad_label, 'l')
  # good.Draw('hist')
  # bad.Draw('hist same')
  # leg.Draw('same')
  # c.SaveAs('total_pulse_soi0_ADC_cut0'+run_num+'.png')

  # good = fi.Get('hist_ho_summedADC_soi0_12_414243_cut15_good')
  # bad = fi.Get('hist_ho_summedADC_soi0_12_414243_cut15_bad')
  # good.GetXaxis().SetTitle(xaxis_ADC)
  # good.GetYaxis().SetTitle(yaxis)
  # good.SetTitle(title_soi0_ADC_cut1)
  # good.GetXaxis().SetRange(1, good.GetBin(ADC_high))
  # bad.GetXaxis().SetRange(1, bad.GetBin(ADC_high))
  # good.Scale(1.0 / good.Integral())
  # bad.Scale(1.0 / bad.Integral())
  # good.SetMinimum(low)
  # good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  # good.SetLineColor(good_color)
  # bad.SetLineColor(bad_color)
  # leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  # leg.AddEntry(good, good_label, 'l')
  # leg.AddEntry(bad, bad_label, 'l')
  # good.Draw('hist')
  # bad.Draw('hist same')
  # leg.Draw('same')
  # c.SaveAs('total_pulse_soi0_ADC_cut1'+run_num+'.png')

  # good = fi.Get('hist_ho_summedADC_soi0_12_414243_cut20_good')
  # bad = fi.Get('hist_ho_summedADC_soi0_12_414243_cut20_bad')
  # good = good.Rebin(rebin)
  # bad = bad.Rebin(rebin)
  # good.GetXaxis().SetTitle(xaxis_ADC)
  # good.GetYaxis().SetTitle(yaxis)
  # good.SetTitle(title_soi0_ADC_cut2)
  # good.GetXaxis().SetRange(1, good.GetBin(ADC_veryhigh/rebin))
  # bad.GetXaxis().SetRange(1, bad.GetBin(ADC_veryhigh/rebin))
  # good.Scale(1.0 / good.Integral())
  # bad.Scale(1.0 / bad.Integral())
  # good.SetMinimum(low)
  # good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  # good.SetLineColor(good_color)
  # bad.SetLineColor(bad_color)
  # leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  # leg.AddEntry(good, good_label, 'l')
  # leg.AddEntry(bad, bad_label, 'l')
  # good.Draw('hist')
  # bad.Draw('hist same')
  # leg.Draw('same')
  # c.SaveAs('total_pulse_soi0_ADC_cut2'+run_num+'.png')

  good = fi.Get('hist_ho_summedADC_soi4_12_414243_nocut_good')
  bad = fi.Get('hist_ho_summedADC_soi4_12_414243_nocut_bad')
  good.GetXaxis().SetTitle(xaxis_ADC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_ADC_cut0)
  good.GetXaxis().SetRange(1, good.GetBin(ADC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(ADC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_ADC_cut0'+run_num+'.png')

  good = fi.Get('hist_ho_summedADC_soi4_12_414243_cut15_good')
  bad = fi.Get('hist_ho_summedADC_soi4_12_414243_cut15_bad')
  good.GetXaxis().SetTitle(xaxis_ADC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_ADC_cut1)
  good.GetXaxis().SetRange(1, good.GetBin(ADC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(ADC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_ADC_cut1'+run_num+'.png')

  good = fi.Get('hist_ho_summedADC_soi4_12_414243_cut20_good')
  bad = fi.Get('hist_ho_summedADC_soi4_12_414243_cut20_bad')
  good = good.Rebin(rebin)
  bad = bad.Rebin(rebin)
  good.GetXaxis().SetTitle(xaxis_ADC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_ADC_cut2)
  good.GetXaxis().SetRange(1, good.GetBin(ADC_veryhigh/rebin))
  bad.GetXaxis().SetRange(1, bad.GetBin(ADC_veryhigh/rebin))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_ADC_cut2'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi0_12_414243_nocut_good')
  bad = fi.Get('hist_ho_summedfC_soi0_12_414243_nocut_bad')
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi0_fC_cut0)
  good.GetXaxis().SetRange(1, good.GetBin(fC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi0_fC_cut0'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi0_12_414243_cut15_good')
  bad = fi.Get('hist_ho_summedfC_soi0_12_414243_cut15_bad')
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi0_fC_cut1)
  good.GetXaxis().SetRange(1, good.GetBin(fC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi0_fC_cut1'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi0_12_414243_cut20_good')
  bad = fi.Get('hist_ho_summedfC_soi0_12_414243_cut20_bad')
  good = good.Rebin(rebin)
  bad = bad.Rebin(rebin)
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi0_fC_cut2)
  good.GetXaxis().SetRange(1, good.GetBin(fC_veryhigh/rebin))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_veryhigh/rebin))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi0_fC_cut2'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi4_12_414243_nocut_good')
  bad = fi.Get('hist_ho_summedfC_soi4_12_414243_nocut_bad')
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_fC_cut0)
  good.GetXaxis().SetRange(1, good.GetBin(fC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_fC_cut0'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi4_12_414243_cut15_good')
  bad = fi.Get('hist_ho_summedfC_soi4_12_414243_cut15_bad')
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_fC_cut1)
  good.GetXaxis().SetRange(1, good.GetBin(fC_high))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_high))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_fC_cut1'+run_num+'.png')

  good = fi.Get('hist_ho_summedfC_soi4_12_414243_cut20_good')
  bad = fi.Get('hist_ho_summedfC_soi4_12_414243_cut20_bad')
  good = good.Rebin(rebin)
  bad = bad.Rebin(rebin)
  good.GetXaxis().SetTitle(xaxis_fC)
  good.GetYaxis().SetTitle(yaxis)
  good.SetTitle(title_soi4_fC_cut2)
  good.GetXaxis().SetRange(1, good.GetBin(fC_veryhigh/rebin))
  bad.GetXaxis().SetRange(1, bad.GetBin(fC_veryhigh/rebin))
  good.Scale(1.0 / good.Integral())
  bad.Scale(1.0 / bad.Integral())
  good.SetMinimum(low)
  good.SetMaximum(max(good.GetMaximum(), bad.GetMaximum()) * 1.1)
  good.SetLineColor(good_color)
  bad.SetLineColor(bad_color)
  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good, good_label, 'l')
  leg.AddEntry(bad, bad_label, 'l')
  good.Draw('hist')
  bad.Draw('hist same')
  leg.Draw('same')
  c.SaveAs('total_pulse_soi4_fC_cut2'+run_num+'.png')

  c.SetLogy(0)


# avg with many lines
#if True:
if False:
  xaxis = 'TS'
  yaxis_ADC = 'ADC'
  yaxis_fC = 'fC'

  cut0_ADC_low = 8.5
  cut0_ADC_high = 11
  cut1_ADC_low = 8.5
  cut1_ADC_high = 11
  cut2_ADC_low = 8.5
  cut2_ADC_high = 16

  cut0_fC_low = 0
  cut0_fC_high = 6
  cut1_fC_low = 0
  cut1_fC_high = 6
  cut2_fC_low = 0
  cut2_fC_high = 30

  ho_title_ADC = 'HO, average ADC in bad channels only'
  ho_title_fC = 'HO, average fC in bad channels only'
  ho_cut0_title_ADC = run_string+ho_title_ADC+''
  ho_cut1_title_ADC = run_string+ho_title_ADC+', cut at 1'
  ho_cut2_title_ADC = run_string+ho_title_ADC+', cut at 2'
  ho_cut0_title_fC = run_string+ho_title_fC+''
  ho_cut1_title_fC = run_string+ho_title_fC+', cut at 1'
  ho_cut2_title_fC = run_string+ho_title_fC+', cut at 2'

  color_40 = kBlue
  color_44 = kBlue
  color_41_good = kBlack
  color_41_bad = kRed
  color_42_good = kBlack
  color_42_bad = kRed
  color_43_good = kBlack
  color_43_bad = kRed

  legend_title = ''
  legend_xi = 0.75
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.9
  legend_40_label = 'iEta 12, iPhi 40'
  legend_44_label = 'iEta 12, iPhi 44'
  legend_41_good_label = 'iEta 12, iPhi 41, good hits'
  legend_41_bad_label = 'iEta 12, iPhi 41, bad hits'
  legend_42_good_label = 'iEta 12, iPhi 42, good hits'
  legend_42_bad_label = 'iEta 12, iPhi 42, bad hits'
  legend_43_good_label = 'iEta 12, iPhi 43, good hits'
  legend_43_bad_label = 'iEta 12, iPhi 43. bad hits'

  ho_cut0_ADC_40 = fi.Get('hist_ho_totADCinTS_nocut_12_40')
  ho_cut0_ADC_44 = fi.Get('hist_ho_totADCinTS_nocut_12_44')
  ho_cut0_ADC_41_good = fi.Get('hist_ho_totADCinTS_nocut_12_41_good')
  ho_cut0_ADC_41_bad = fi.Get('hist_ho_totADCinTS_nocut_12_41_bad')
  ho_cut0_ADC_42_good = fi.Get('hist_ho_totADCinTS_nocut_12_42_good')
  ho_cut0_ADC_42_bad = fi.Get('hist_ho_totADCinTS_nocut_12_42_bad')
  ho_cut0_ADC_43_good = fi.Get('hist_ho_totADCinTS_nocut_12_43_good')
  ho_cut0_ADC_43_bad = fi.Get('hist_ho_totADCinTS_nocut_12_43_bad')

  ho_cut0_ADC_40.SetLineColor(color_40)
  ho_cut0_ADC_44.SetLineColor(color_44)
  ho_cut0_ADC_41_good.SetLineColor(color_41_good)
  ho_cut0_ADC_41_bad.SetLineColor(color_41_bad)
  ho_cut0_ADC_42_good.SetLineColor(color_42_good)
  ho_cut0_ADC_42_bad.SetLineColor(color_42_bad)
  ho_cut0_ADC_43_good.SetLineColor(color_43_good)
  ho_cut0_ADC_43_bad.SetLineColor(color_43_bad)

  ho_cut0_ADC_40.Scale(10.0 / ho_cut0_ADC_40.GetEntries() )
  ho_cut0_ADC_44.Scale(10.0 / ho_cut0_ADC_44.GetEntries() )
  ho_cut0_ADC_41_good.Scale(10.0 / ho_cut0_ADC_41_good.GetEntries() )
  ho_cut0_ADC_41_bad.Scale(10.0 / ho_cut0_ADC_41_bad.GetEntries() )
  ho_cut0_ADC_42_good.Scale(10.0 / ho_cut0_ADC_42_good.GetEntries() )
  ho_cut0_ADC_42_bad.Scale(10.0 / ho_cut0_ADC_42_bad.GetEntries() )
  ho_cut0_ADC_43_good.Scale(10.0 / ho_cut0_ADC_43_good.GetEntries() )
  ho_cut0_ADC_43_bad.Scale(10.0 / ho_cut0_ADC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_ADC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut0_ADC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut0_ADC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut0_ADC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut0_ADC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut0_ADC_44, legend_44_label, 'l')

  ho_cut0_ADC_40.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC_40.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC_40.SetTitle(ho_cut0_title_ADC)
  ho_cut0_ADC_40.SetMaximum(cut0_ADC_high)
  ho_cut0_ADC_40.SetMinimum(cut0_ADC_low)
  ho_cut0_ADC_40.Draw()
  ho_cut0_ADC_44.Draw('same')
  ho_cut0_ADC_41_good.Draw('same')
  ho_cut0_ADC_41_bad.Draw('same')
  ho_cut0_ADC_42_good.Draw('same')
  ho_cut0_ADC_42_bad.Draw('same')
  ho_cut0_ADC_43_good.Draw('same')
  ho_cut0_ADC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgADC_badchannels_compare_cut0'+run_num+'.png')

  ho_cut1_ADC_40 = fi.Get('hist_ho_totADCinTS_cut15_12_40')
  ho_cut1_ADC_44 = fi.Get('hist_ho_totADCinTS_cut15_12_44')
  ho_cut1_ADC_41_good = fi.Get('hist_ho_totADCinTS_cut15_12_41_good')
  ho_cut1_ADC_41_bad = fi.Get('hist_ho_totADCinTS_cut15_12_41_bad')
  ho_cut1_ADC_42_good = fi.Get('hist_ho_totADCinTS_cut15_12_42_good')
  ho_cut1_ADC_42_bad = fi.Get('hist_ho_totADCinTS_cut15_12_42_bad')
  ho_cut1_ADC_43_good = fi.Get('hist_ho_totADCinTS_cut15_12_43_good')
  ho_cut1_ADC_43_bad = fi.Get('hist_ho_totADCinTS_cut15_12_43_bad')

  ho_cut1_ADC_40.SetLineColor(color_40)
  ho_cut1_ADC_44.SetLineColor(color_44)
  ho_cut1_ADC_41_good.SetLineColor(color_41_good)
  ho_cut1_ADC_41_bad.SetLineColor(color_41_bad)
  ho_cut1_ADC_42_good.SetLineColor(color_42_good)
  ho_cut1_ADC_42_bad.SetLineColor(color_42_bad)
  ho_cut1_ADC_43_good.SetLineColor(color_43_good)
  ho_cut1_ADC_43_bad.SetLineColor(color_43_bad)

  ho_cut1_ADC_40.Scale(10.0 / ho_cut1_ADC_40.GetEntries() )
  ho_cut1_ADC_44.Scale(10.0 / ho_cut1_ADC_44.GetEntries() )
  ho_cut1_ADC_41_good.Scale(10.0 / ho_cut1_ADC_41_good.GetEntries() )
  ho_cut1_ADC_41_bad.Scale(10.0 / ho_cut1_ADC_41_bad.GetEntries() )
  ho_cut1_ADC_42_good.Scale(10.0 / ho_cut1_ADC_42_good.GetEntries() )
  ho_cut1_ADC_42_bad.Scale(10.0 / ho_cut1_ADC_42_bad.GetEntries() )
  ho_cut1_ADC_43_good.Scale(10.0 / ho_cut1_ADC_43_good.GetEntries() )
  ho_cut1_ADC_43_bad.Scale(10.0 / ho_cut1_ADC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut1_ADC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut1_ADC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut1_ADC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut1_ADC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut1_ADC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut1_ADC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut1_ADC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut1_ADC_44, legend_44_label, 'l')

  ho_cut1_ADC_40.GetXaxis().SetTitle(xaxis)
  ho_cut1_ADC_40.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut1_ADC_40.SetTitle(ho_cut1_title_ADC)
  ho_cut1_ADC_40.SetMaximum(cut1_ADC_high)
  ho_cut1_ADC_40.SetMinimum(cut1_ADC_low)
  ho_cut1_ADC_40.Draw()
  ho_cut1_ADC_44.Draw('same')
  ho_cut1_ADC_41_good.Draw('same')
  ho_cut1_ADC_41_bad.Draw('same')
  ho_cut1_ADC_42_good.Draw('same')
  ho_cut1_ADC_42_bad.Draw('same')
  ho_cut1_ADC_43_good.Draw('same')
  ho_cut1_ADC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgADC_badchannels_compare_cut1'+run_num+'.png')

  ho_cut2_ADC_40 = fi.Get('hist_ho_totADCinTS_cut20_12_40')
  ho_cut2_ADC_44 = fi.Get('hist_ho_totADCinTS_cut20_12_44')
  ho_cut2_ADC_41_good = fi.Get('hist_ho_totADCinTS_cut20_12_41_good')
  ho_cut2_ADC_41_bad = fi.Get('hist_ho_totADCinTS_cut20_12_41_bad')
  ho_cut2_ADC_42_good = fi.Get('hist_ho_totADCinTS_cut20_12_42_good')
  ho_cut2_ADC_42_bad = fi.Get('hist_ho_totADCinTS_cut20_12_42_bad')
  ho_cut2_ADC_43_good = fi.Get('hist_ho_totADCinTS_cut20_12_43_good')
  ho_cut2_ADC_43_bad = fi.Get('hist_ho_totADCinTS_cut20_12_43_bad')

  ho_cut2_ADC_40.SetLineColor(color_40)
  ho_cut2_ADC_44.SetLineColor(color_44)
  ho_cut2_ADC_41_good.SetLineColor(color_41_good)
  ho_cut2_ADC_41_bad.SetLineColor(color_41_bad)
  ho_cut2_ADC_42_good.SetLineColor(color_42_good)
  ho_cut2_ADC_42_bad.SetLineColor(color_42_bad)
  ho_cut2_ADC_43_good.SetLineColor(color_43_good)
  ho_cut2_ADC_43_bad.SetLineColor(color_43_bad)

  ho_cut2_ADC_40.Scale(10.0 / ho_cut2_ADC_40.GetEntries() )
  ho_cut2_ADC_44.Scale(10.0 / ho_cut2_ADC_44.GetEntries() )
  ho_cut2_ADC_41_good.Scale(10.0 / ho_cut2_ADC_41_good.GetEntries() )
  ho_cut2_ADC_41_bad.Scale(10.0 / ho_cut2_ADC_41_bad.GetEntries() )
  ho_cut2_ADC_42_good.Scale(10.0 / ho_cut2_ADC_42_good.GetEntries() )
  ho_cut2_ADC_42_bad.Scale(10.0 / ho_cut2_ADC_42_bad.GetEntries() )
  ho_cut2_ADC_43_good.Scale(10.0 / ho_cut2_ADC_43_good.GetEntries() )
  ho_cut2_ADC_43_bad.Scale(10.0 / ho_cut2_ADC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut2_ADC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut2_ADC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut2_ADC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut2_ADC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut2_ADC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut2_ADC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut2_ADC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut2_ADC_44, legend_44_label, 'l')

  ho_cut2_ADC_40.GetXaxis().SetTitle(xaxis)
  ho_cut2_ADC_40.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut2_ADC_40.SetTitle(ho_cut2_title_ADC)
  ho_cut2_ADC_40.SetMaximum(cut2_ADC_high)
  ho_cut2_ADC_40.SetMinimum(cut2_ADC_low)
  ho_cut2_ADC_40.Draw()
  ho_cut2_ADC_44.Draw('same')
  ho_cut2_ADC_41_good.Draw('same')
  ho_cut2_ADC_41_bad.Draw('same')
  ho_cut2_ADC_42_good.Draw('same')
  ho_cut2_ADC_42_bad.Draw('same')
  ho_cut2_ADC_43_good.Draw('same')
  ho_cut2_ADC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgADC_badchannels_compare_cut2'+run_num+'.png')

  ho_cut0_fC_40 = fi.Get('hist_ho_totfCinTS_nocut_12_40')
  ho_cut0_fC_44 = fi.Get('hist_ho_totfCinTS_nocut_12_44')
  ho_cut0_fC_41_good = fi.Get('hist_ho_totfCinTS_nocut_12_41_good')
  ho_cut0_fC_41_bad = fi.Get('hist_ho_totfCinTS_nocut_12_41_bad')
  ho_cut0_fC_42_good = fi.Get('hist_ho_totfCinTS_nocut_12_42_good')
  ho_cut0_fC_42_bad = fi.Get('hist_ho_totfCinTS_nocut_12_42_bad')
  ho_cut0_fC_43_good = fi.Get('hist_ho_totfCinTS_nocut_12_43_good')
  ho_cut0_fC_43_bad = fi.Get('hist_ho_totfCinTS_nocut_12_43_bad')

  ho_cut0_fC_40.SetLineColor(color_40)
  ho_cut0_fC_44.SetLineColor(color_44)
  ho_cut0_fC_41_good.SetLineColor(color_41_good)
  ho_cut0_fC_41_bad.SetLineColor(color_41_bad)
  ho_cut0_fC_42_good.SetLineColor(color_42_good)
  ho_cut0_fC_42_bad.SetLineColor(color_42_bad)
  ho_cut0_fC_43_good.SetLineColor(color_43_good)
  ho_cut0_fC_43_bad.SetLineColor(color_43_bad)

  ho_cut0_fC_40.Scale(10.0 / ho_cut0_fC_40.GetEntries() )
  ho_cut0_fC_44.Scale(10.0 / ho_cut0_fC_44.GetEntries() )
  ho_cut0_fC_41_good.Scale(10.0 / ho_cut0_fC_41_good.GetEntries() )
  ho_cut0_fC_41_bad.Scale(10.0 / ho_cut0_fC_41_bad.GetEntries() )
  ho_cut0_fC_42_good.Scale(10.0 / ho_cut0_fC_42_good.GetEntries() )
  ho_cut0_fC_42_bad.Scale(10.0 / ho_cut0_fC_42_bad.GetEntries() )
  ho_cut0_fC_43_good.Scale(10.0 / ho_cut0_fC_43_good.GetEntries() )
  ho_cut0_fC_43_bad.Scale(10.0 / ho_cut0_fC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_fC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut0_fC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut0_fC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut0_fC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut0_fC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut0_fC_44, legend_44_label, 'l')

  ho_cut0_fC_40.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC_40.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC_40.SetTitle(ho_cut0_title_fC)
  ho_cut0_fC_40.SetMaximum(cut0_fC_high)
  ho_cut0_fC_40.SetMinimum(cut0_fC_low)
  ho_cut0_fC_40.Draw()
  ho_cut0_fC_44.Draw('same')
  ho_cut0_fC_41_good.Draw('same')
  ho_cut0_fC_41_bad.Draw('same')
  ho_cut0_fC_42_good.Draw('same')
  ho_cut0_fC_42_bad.Draw('same')
  ho_cut0_fC_43_good.Draw('same')
  ho_cut0_fC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgfC_badchannels_compare_cut0'+run_num+'.png')

  ho_cut1_fC_40 = fi.Get('hist_ho_totfCinTS_cut15_12_40')
  ho_cut1_fC_44 = fi.Get('hist_ho_totfCinTS_cut15_12_44')
  ho_cut1_fC_41_good = fi.Get('hist_ho_totfCinTS_cut15_12_41_good')
  ho_cut1_fC_41_bad = fi.Get('hist_ho_totfCinTS_cut15_12_41_bad')
  ho_cut1_fC_42_good = fi.Get('hist_ho_totfCinTS_cut15_12_42_good')
  ho_cut1_fC_42_bad = fi.Get('hist_ho_totfCinTS_cut15_12_42_bad')
  ho_cut1_fC_43_good = fi.Get('hist_ho_totfCinTS_cut15_12_43_good')
  ho_cut1_fC_43_bad = fi.Get('hist_ho_totfCinTS_cut15_12_43_bad')

  ho_cut1_fC_40.SetLineColor(color_40)
  ho_cut1_fC_44.SetLineColor(color_44)
  ho_cut1_fC_41_good.SetLineColor(color_41_good)
  ho_cut1_fC_41_bad.SetLineColor(color_41_bad)
  ho_cut1_fC_42_good.SetLineColor(color_42_good)
  ho_cut1_fC_42_bad.SetLineColor(color_42_bad)
  ho_cut1_fC_43_good.SetLineColor(color_43_good)
  ho_cut1_fC_43_bad.SetLineColor(color_43_bad)

  ho_cut1_fC_40.Scale(10.0 / ho_cut1_fC_40.GetEntries() )
  ho_cut1_fC_44.Scale(10.0 / ho_cut1_fC_44.GetEntries() )
  ho_cut1_fC_41_good.Scale(10.0 / ho_cut1_fC_41_good.GetEntries() )
  ho_cut1_fC_41_bad.Scale(10.0 / ho_cut1_fC_41_bad.GetEntries() )
  ho_cut1_fC_42_good.Scale(10.0 / ho_cut1_fC_42_good.GetEntries() )
  ho_cut1_fC_42_bad.Scale(10.0 / ho_cut1_fC_42_bad.GetEntries() )
  ho_cut1_fC_43_good.Scale(10.0 / ho_cut1_fC_43_good.GetEntries() )
  ho_cut1_fC_43_bad.Scale(10.0 / ho_cut1_fC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut1_fC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut1_fC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut1_fC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut1_fC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut1_fC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut1_fC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut1_fC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut1_fC_44, legend_44_label, 'l')

  ho_cut1_fC_40.GetXaxis().SetTitle(xaxis)
  ho_cut1_fC_40.GetYaxis().SetTitle(yaxis_fC)
  ho_cut1_fC_40.SetTitle(ho_cut1_title_fC)
  ho_cut1_fC_40.SetMaximum(cut1_fC_high)
  ho_cut1_fC_40.SetMinimum(cut1_fC_low)
  ho_cut1_fC_40.Draw()
  ho_cut1_fC_44.Draw('same')
  ho_cut1_fC_41_good.Draw('same')
  ho_cut1_fC_41_bad.Draw('same')
  ho_cut1_fC_42_good.Draw('same')
  ho_cut1_fC_42_bad.Draw('same')
  ho_cut1_fC_43_good.Draw('same')
  ho_cut1_fC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgfC_badchannels_compare_cut1'+run_num+'.png')

  ho_cut2_fC_40 = fi.Get('hist_ho_totfCinTS_cut20_12_40')
  ho_cut2_fC_44 = fi.Get('hist_ho_totfCinTS_cut20_12_44')
  ho_cut2_fC_41_good = fi.Get('hist_ho_totfCinTS_cut20_12_41_good')
  ho_cut2_fC_41_bad = fi.Get('hist_ho_totfCinTS_cut20_12_41_bad')
  ho_cut2_fC_42_good = fi.Get('hist_ho_totfCinTS_cut20_12_42_good')
  ho_cut2_fC_42_bad = fi.Get('hist_ho_totfCinTS_cut20_12_42_bad')
  ho_cut2_fC_43_good = fi.Get('hist_ho_totfCinTS_cut20_12_43_good')
  ho_cut2_fC_43_bad = fi.Get('hist_ho_totfCinTS_cut20_12_43_bad')

  ho_cut2_fC_40.SetLineColor(color_40)
  ho_cut2_fC_44.SetLineColor(color_44)
  ho_cut2_fC_41_good.SetLineColor(color_41_good)
  ho_cut2_fC_41_bad.SetLineColor(color_41_bad)
  ho_cut2_fC_42_good.SetLineColor(color_42_good)
  ho_cut2_fC_42_bad.SetLineColor(color_42_bad)
  ho_cut2_fC_43_good.SetLineColor(color_43_good)
  ho_cut2_fC_43_bad.SetLineColor(color_43_bad)

  ho_cut2_fC_40.Scale(10.0 / ho_cut2_fC_40.GetEntries() )
  ho_cut2_fC_44.Scale(10.0 / ho_cut2_fC_44.GetEntries() )
  ho_cut2_fC_41_good.Scale(10.0 / ho_cut2_fC_41_good.GetEntries() )
  ho_cut2_fC_41_bad.Scale(10.0 / ho_cut2_fC_41_bad.GetEntries() )
  ho_cut2_fC_42_good.Scale(10.0 / ho_cut2_fC_42_good.GetEntries() )
  ho_cut2_fC_42_bad.Scale(10.0 / ho_cut2_fC_42_bad.GetEntries() )
  ho_cut2_fC_43_good.Scale(10.0 / ho_cut2_fC_43_good.GetEntries() )
  ho_cut2_fC_43_bad.Scale(10.0 / ho_cut2_fC_43_bad.GetEntries() )

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut2_fC_40, legend_40_label, 'l')
  leg.AddEntry(ho_cut2_fC_41_good, legend_41_good_label, 'l')
  leg.AddEntry(ho_cut2_fC_42_good, legend_42_good_label, 'l')
  leg.AddEntry(ho_cut2_fC_43_good, legend_43_good_label, 'l')
  leg.AddEntry(ho_cut2_fC_41_bad, legend_41_bad_label, 'l')
  leg.AddEntry(ho_cut2_fC_42_bad, legend_42_bad_label, 'l')
  leg.AddEntry(ho_cut2_fC_43_bad, legend_43_bad_label, 'l')
  leg.AddEntry(ho_cut2_fC_44, legend_44_label, 'l')

  ho_cut2_fC_40.GetXaxis().SetTitle(xaxis)
  ho_cut2_fC_40.GetYaxis().SetTitle(yaxis_fC)
  ho_cut2_fC_40.SetTitle(ho_cut2_title_fC)
  ho_cut2_fC_40.SetMaximum(cut2_fC_high)
  ho_cut2_fC_40.SetMinimum(cut2_fC_low)
  ho_cut2_fC_40.Draw()
  ho_cut2_fC_44.Draw('same')
  ho_cut2_fC_41_good.Draw('same')
  ho_cut2_fC_41_bad.Draw('same')
  ho_cut2_fC_42_good.Draw('same')
  ho_cut2_fC_42_bad.Draw('same')
  ho_cut2_fC_43_good.Draw('same')
  ho_cut2_fC_43_bad.Draw('same')
  leg.Draw('same')

  c.SaveAs('avgfC_badchannels_compare_cut2'+run_num+'.png')


# 2d full dsitribution plots
if False:
  xaxis = 'TS'
  yaxis_ADC = 'ADC'
  yaxis_fC = 'fC'
  ho_title_cut0_ADC = run_string+'HO, ADC full distribution'
  ho_title_cut1_ADC = run_string+'HO, ADC full distribution, at least one pulse > ADC 15'
  ho_title_cut2_ADC = run_string+'HO, ADC full distribution, at least one pulse > ADC 20'
  hb_title_cut0_ADC = run_string+'HB, ADC full distribution'
  hb_title_cut1_ADC = run_string+'HB, ADC full distribution, at least one pulse > ADC 5'
  hb_title_cut2_ADC = run_string+'HB, ADC full distribution, at least one pulse > ADC 8'
  he_title_cut0_ADC = run_string+'HE, ADC full distribution'
  he_title_cut1_ADC = run_string+'HE, ADC full distribution, at least one pulse > ADC 10'
  he_title_cut2_ADC = run_string+'HE, ADC full distribution, at least one pulse > ADC 15'
  ho_title_cut0_fC = run_string+'HO, fC full distribution'
  ho_title_cut1_fC = run_string+'HO, fC full distribution, at least one pulse > ADC 15'
  ho_title_cut2_fC = run_string+'HO, fC full distribution, at least one pulse > ADC 20'
  hb_title_cut0_fC = run_string+'HB, fC full distribution'
  hb_title_cut1_fC = run_string+'HB, fC full distribution, at least one pulse > ADC 5'
  hb_title_cut2_fC = run_string+'HB, fC full distribution, at least one pulse > ADC 8'
  he_title_cut0_fC = run_string+'HE, fC full distribution'
  he_title_cut1_fC = run_string+'HE, fC full distribution, at least one pulse > ADC 10'
  he_title_cut2_fC = run_string+'HE, fC full distribution, at least one pulse > ADC 15'

  he_high_ADC = 200
  hb_high_ADC = 200
  ho_high_ADC = 200
  he_high_fC = 100
  hb_high_fC = 100
  ho_high_fC = 100

  he_cut0_ADC = fi.Get('hist_he_allADCinTS_nocut')
  he_cut1_ADC = fi.Get('hist_he_allADCinTS_cut10')
  he_cut2_ADC = fi.Get('hist_he_allADCinTS_cut15')

  ho_cut0_ADC = fi.Get('hist_ho_allADCinTS_nocut')
  ho_cut1_ADC = fi.Get('hist_ho_allADCinTS_cut15')
  ho_cut2_ADC = fi.Get('hist_ho_allADCinTS_cut20')

  hb_cut0_ADC = fi.Get('hist_hb_allADCinTS_nocut')
  hb_cut1_ADC = fi.Get('hist_hb_allADCinTS_cut5')
  hb_cut2_ADC = fi.Get('hist_hb_allADCinTS_cut8')

  he_cut0_fC = fi.Get('hist_he_allfCinTS_nocut')
  he_cut1_fC = fi.Get('hist_he_allfCinTS_cut10')
  he_cut2_fC = fi.Get('hist_he_allfCinTS_cut15')

  ho_cut0_fC = fi.Get('hist_ho_allfCinTS_nocut')
  ho_cut1_fC = fi.Get('hist_ho_allfCinTS_cut15')
  ho_cut2_fC = fi.Get('hist_ho_allfCinTS_cut20')

  hb_cut0_fC = fi.Get('hist_hb_allfCinTS_nocut')
  hb_cut1_fC = fi.Get('hist_hb_allfCinTS_cut5')
  hb_cut2_fC = fi.Get('hist_hb_allfCinTS_cut8')

  he_cut0_ADC.GetXaxis().SetTitle(xaxis)
  he_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut0_ADC.SetTitle(he_title_cut0_ADC)
  he_cut0_ADC.GetYaxis().SetRange(1, he_high_ADC)
  he_cut0_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut0_ADC"+run_num+".png")
  he_cut0_ADC.Write()

  he_cut1_ADC.GetXaxis().SetTitle(xaxis)
  he_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut1_ADC.SetTitle(he_title_cut1_ADC)
  he_cut1_ADC.GetYaxis().SetRange(1, he_high_ADC)
  he_cut1_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut1_ADC"+run_num+".png")
  he_cut1_ADC.Write()

  he_cut2_ADC.GetXaxis().SetTitle(xaxis)
  he_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut2_ADC.SetTitle(he_title_cut2_ADC)
  he_cut2_ADC.GetYaxis().SetRange(1, he_high_ADC)
  he_cut2_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut2_ADC"+run_num+".png")
  he_cut2_ADC.Write()

  hb_cut0_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut0_ADC.SetTitle(he_title_cut0_ADC)
  hb_cut0_ADC.GetYaxis().SetRange(1, hb_high_ADC)
  hb_cut0_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut0_ADC"+run_num+".png")
  hb_cut0_ADC.Write()

  hb_cut1_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut1_ADC.SetTitle(hb_title_cut1_ADC)
  hb_cut1_ADC.GetYaxis().SetRange(1, hb_high_ADC)
  hb_cut1_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut1_ADC"+run_num+".png")
  hb_cut1_ADC.Write()

  hb_cut2_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut2_ADC.SetTitle(hb_title_cut2_ADC)
  hb_cut2_ADC.GetYaxis().SetRange(1, hb_high_ADC)
  hb_cut2_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut2_ADC"+run_num+".png")
  hb_cut2_ADC.Write()

  ho_cut0_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC.SetTitle(ho_title_cut0_ADC)
  ho_cut0_ADC.GetYaxis().SetRange(1, ho_high_ADC)
  ho_cut0_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut0_ADC"+run_num+".png")
  ho_cut0_ADC.Write()

  ho_cut1_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut1_ADC.SetTitle(ho_title_cut1_ADC)
  ho_cut1_ADC.GetYaxis().SetRange(1, ho_high_ADC)
  ho_cut1_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut1_ADC"+run_num+".png")
  ho_cut1_ADC.Write()

  ho_cut2_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut2_ADC.SetTitle(ho_title_cut2_ADC)
  ho_cut2_ADC.GetYaxis().SetRange(1, ho_high_ADC)
  ho_cut2_ADC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut2_ADC"+run_num+".png")
  ho_cut2_ADC.Write()

  he_cut0_fC.GetXaxis().SetTitle(xaxis)
  he_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut0_fC.SetTitle(he_title_cut0_fC)
  he_cut0_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut0_fC"+run_num+".png")
  he_cut0_fC.Write()

  he_cut1_fC.GetXaxis().SetTitle(xaxis)
  he_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut1_fC.SetTitle(he_title_cut1_fC)
  he_cut1_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut1_fC"+run_num+".png")
  he_cut1_fC.Write()

  he_cut2_fC.GetXaxis().SetTitle(xaxis)
  he_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut2_fC.SetTitle(he_title_cut2_fC)
  he_cut2_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_he_cut2_fC"+run_num+".png")
  he_cut2_fC.Write()

  hb_cut0_fC.GetXaxis().SetTitle(xaxis)
  hb_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut0_fC.SetTitle(hb_title_cut0_fC)
  hb_cut0_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut0_fC"+run_num+".png")
  hb_cut0_fC.Write()

  hb_cut1_fC.GetXaxis().SetTitle(xaxis)
  hb_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut1_fC.SetTitle(hb_title_cut1_fC)
  hb_cut1_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut1_fC"+run_num+".png")
  hb_cut1_fC.Write()

  hb_cut2_fC.GetXaxis().SetTitle(xaxis)
  hb_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut2_fC.SetTitle(hb_title_cut2_fC)
  hb_cut2_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_hb_cut2_fC"+run_num+".png")
  hb_cut2_fC.Write()

  ho_cut0_fC.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC.SetTitle(ho_title_cut0_fC)
  ho_cut0_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut0_fC"+run_num+".png")
  ho_cut0_fC.Write()

  ho_cut1_fC.GetXaxis().SetTitle(xaxis)
  ho_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut1_fC.SetTitle(ho_title_cut1_fC)
  ho_cut1_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut1_fC"+run_num+".png")
  ho_cut1_fC.Write()

  ho_cut2_fC.GetXaxis().SetTitle(xaxis)
  ho_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut2_fC.SetTitle(ho_title_cut2_fC)
  ho_cut2_fC.Draw('Colz')
  c.SaveAs("2d_fulldist_ho_cut2_fC"+run_num+".png")
  ho_cut2_fC.Write()

# percent bad per LS
if True:
#if False:
  xaxis = 'LS' 
  yaxis = '% bad hits'
  title = run_string+'precentage of bad hits across all three channels'

  numer = fi.Get('hist_ho_numbadperls')
  denom = fi.Get('hist_ho_numtotperls')

  numer.Divide(denom)
  numer.GetXaxis().SetTitle(xaxis)
  numer.GetYaxis().SetTitle(yaxis)
  numer.GetXaxis().SetRange(LS_low, LS_high)
  numer.SetTitle(title)
  numer.Draw('][')
  c.SaveAs("percentage_bad"+run_num+".png")
  numer.Write()

# ieta vs iphi bad hits
if True:
#if False:
  xaxis = 'iEta' 
  yaxis = 'iPhi'
  title = run_string+'Location of bad hits'

  hist = fi.Get('hist_ho_badhits_etaphi')

  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)
  hist.SetTitle(title)
  hist.Draw('Colz')
  c.SaveAs("ieta_vs_iphi_locbad"+run_num+".png")
  hist.Write()

# average in TS
if True:
#if False:
  xaxis = 'TS'
  yaxis_ADC = 'avg ADC'
  yaxis_fC = 'avg fC'
  ho_title_ADC = run_string+'HO, averge ADC per TS in pulse'
  ho_title_fC = run_string+'HO, averge fC per TS in pulse'
  he_title_ADC = run_string+'HE, averge ADC per TS in pulse'
  he_title_fC = run_string+'HE, averge fC per TS in pulse'
  hb_title_ADC = run_string+'HB, averge ADC per TS in pulse'
  hb_title_fC = run_string+'HB, averge fC per TS in pulse'
  ho_high = 40
  he_high_ADC = 50
  he_high_fC = 1400
  hb_high = 20
  legend_title = ''
  legend_xi = 0.7
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.8
  legend_cut0_label = 'cut 0'
  legend_cut1_label = 'cut 1'
  legend_cut2_label = 'cut 2'
  cut0_color = kViolet
  cut1_color = kGreen
  cut2_color = kBlue

  ho_cut0_ADC = fi.Get('hist_ho_totADCinTS_nocut')
  ho_cut0_ADC.Scale(10.0 / ho_cut0_ADC.GetEntries() )
  ho_cut0_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut0_ADC.SetTitle(ho_title_ADC)
  ho_cut0_ADC.SetMinimum(0)
  ho_cut0_ADC.SetMaximum(ho_high)
  ho_cut0_ADC.SetLineColor(cut0_color)
  ho_cut0_ADC.Draw('')

  ho_cut1_ADC = fi.Get('hist_ho_totADCinTS_cut15')
  ho_cut1_ADC.Scale(10.0 / ho_cut1_ADC.GetEntries() )
  ho_cut1_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut1_ADC.SetTitle(ho_title_ADC)
  ho_cut1_ADC.SetLineColor(cut1_color)
  ho_cut1_ADC.Draw('same')

  ho_cut2_ADC = fi.Get('hist_ho_totADCinTS_cut20')
  ho_cut2_ADC.Scale(10.0 / ho_cut2_ADC.GetEntries() )
  ho_cut2_ADC.GetXaxis().SetTitle(xaxis)
  ho_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  ho_cut2_ADC.SetTitle(ho_title_ADC)
  ho_cut2_ADC.SetLineColor(cut2_color)
  ho_cut2_ADC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_ADC, legend_cut0_label, 'l')
  leg.AddEntry(ho_cut1_ADC, legend_cut1_label, 'l')
  leg.AddEntry(ho_cut2_ADC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("ho_avgADC"+run_num+".png")

  ho_cut0_fC = fi.Get('hist_ho_totfCinTS_nocut')
  ho_cut0_fC.Scale(10.0 / ho_cut0_fC.GetEntries() )
  ho_cut0_fC.GetXaxis().SetTitle(xaxis)
  ho_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut0_fC.SetTitle(ho_title_fC)
  ho_cut0_fC.SetMinimum(0)
  ho_cut0_fC.SetMaximum(ho_high)
  ho_cut0_fC.SetLineColor(cut0_color)
  ho_cut0_fC.Draw('')

  ho_cut1_fC = fi.Get('hist_ho_totfCinTS_cut15')
  ho_cut1_fC.Scale(10.0 / ho_cut1_fC.GetEntries() )
  ho_cut1_fC.GetXaxis().SetTitle(xaxis)
  ho_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut1_fC.SetTitle(ho_title_fC)
  ho_cut1_fC.SetLineColor(cut1_color)
  ho_cut1_fC.Draw('same')

  ho_cut2_fC = fi.Get('hist_ho_totfCinTS_cut20')
  ho_cut2_fC.Scale(10.0 / ho_cut2_fC.GetEntries() )
  ho_cut2_fC.GetXaxis().SetTitle(xaxis)
  ho_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  ho_cut2_fC.SetTitle(ho_title_fC)
  ho_cut2_fC.SetLineColor(cut2_color)
  ho_cut2_fC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(ho_cut0_fC, legend_cut0_label, 'l')
  leg.AddEntry(ho_cut1_fC, legend_cut1_label, 'l')
  leg.AddEntry(ho_cut2_fC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("ho_avgfC"+run_num+".png")

  he_cut0_ADC = fi.Get('hist_he_totADCinTS_nocut')
  he_cut0_ADC.Scale(10.0 / he_cut0_ADC.GetEntries() )
  he_cut0_ADC.GetXaxis().SetTitle(xaxis)
  he_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut0_ADC.SetTitle(he_title_ADC)
  he_cut0_ADC.SetMinimum(0)
  he_cut0_ADC.SetMaximum(he_high_ADC)
  he_cut0_ADC.SetLineColor(cut0_color)
  he_cut0_ADC.Draw('')

  he_cut1_ADC = fi.Get('hist_he_totADCinTS_cut10')
  he_cut1_ADC.Scale(10.0 / he_cut1_ADC.GetEntries() )
  he_cut1_ADC.GetXaxis().SetTitle(xaxis)
  he_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut1_ADC.SetTitle(he_title_ADC)
  he_cut1_ADC.SetLineColor(cut1_color)
  he_cut1_ADC.Draw('same')

  he_cut2_ADC = fi.Get('hist_he_totADCinTS_cut15')
  he_cut2_ADC.Scale(10.0 / he_cut2_ADC.GetEntries() )
  he_cut2_ADC.GetXaxis().SetTitle(xaxis)
  he_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  he_cut2_ADC.SetTitle(he_title_ADC)
  he_cut2_ADC.SetLineColor(cut2_color)
  he_cut2_ADC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(he_cut0_ADC, legend_cut0_label, 'l')
  leg.AddEntry(he_cut1_ADC, legend_cut1_label, 'l')
  leg.AddEntry(he_cut2_ADC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("he_avgADC"+run_num+".png")

  he_cut0_fC = fi.Get('hist_he_totfCinTS_nocut')
  he_cut0_fC.Scale(10.0 / he_cut0_fC.GetEntries() )
  he_cut0_fC.GetXaxis().SetTitle(xaxis)
  he_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut0_fC.SetTitle(he_title_fC)
  he_cut0_fC.SetMinimum(0)
  he_cut0_fC.SetMaximum(he_high_fC)
  he_cut0_fC.SetLineColor(cut0_color)
  he_cut0_fC.Draw('')

  he_cut1_fC = fi.Get('hist_he_totfCinTS_cut10')
  he_cut1_fC.Scale(10.0 / he_cut1_fC.GetEntries() )
  he_cut1_fC.GetXaxis().SetTitle(xaxis)
  he_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut1_fC.SetTitle(he_title_fC)
  he_cut1_fC.SetLineColor(cut1_color)
  he_cut1_fC.Draw('same')

  he_cut2_fC = fi.Get('hist_he_totfCinTS_cut15')
  he_cut2_fC.Scale(10.0 / he_cut2_fC.GetEntries() )
  he_cut2_fC.GetXaxis().SetTitle(xaxis)
  he_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  he_cut2_fC.SetTitle(he_title_fC)
  he_cut2_fC.SetLineColor(cut2_color)
  he_cut2_fC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(he_cut0_fC, legend_cut0_label, 'l')
  leg.AddEntry(he_cut1_fC, legend_cut1_label, 'l')
  leg.AddEntry(he_cut2_fC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("he_avgfC"+run_num+".png")

  hb_cut0_ADC = fi.Get('hist_hb_totADCinTS_nocut')
  hb_cut0_ADC.Scale(10.0 / hb_cut0_ADC.GetEntries() )
  hb_cut0_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut0_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut0_ADC.SetTitle(hb_title_ADC)
  hb_cut0_ADC.SetMinimum(0)
  hb_cut0_ADC.SetMaximum(hb_high)
  hb_cut0_ADC.SetLineColor(cut0_color)
  hb_cut0_ADC.Draw('')

  hb_cut1_ADC = fi.Get('hist_hb_totADCinTS_cut5')
  hb_cut1_ADC.Scale(10.0 / hb_cut1_ADC.GetEntries() )
  hb_cut1_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut1_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut1_ADC.SetTitle(hb_title_ADC)
  hb_cut1_ADC.SetLineColor(cut1_color)
  hb_cut1_ADC.Draw('same')

  hb_cut2_ADC = fi.Get('hist_hb_totADCinTS_cut8')
  hb_cut2_ADC.Scale(10.0 / hb_cut2_ADC.GetEntries() )
  hb_cut2_ADC.GetXaxis().SetTitle(xaxis)
  hb_cut2_ADC.GetYaxis().SetTitle(yaxis_ADC)
  hb_cut2_ADC.SetTitle(hb_title_ADC)
  hb_cut2_ADC.SetLineColor(cut2_color)
  hb_cut2_ADC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(hb_cut0_ADC, legend_cut0_label, 'l')
  leg.AddEntry(hb_cut1_ADC, legend_cut1_label, 'l')
  leg.AddEntry(hb_cut2_ADC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("hb_avgADC"+run_num+".png")

  hb_cut0_fC = fi.Get('hist_hb_totfCinTS_nocut')
  hb_cut0_fC.Scale(10.0 / hb_cut0_fC.GetEntries() )
  hb_cut0_fC.GetXaxis().SetTitle(xaxis)
  hb_cut0_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut0_fC.SetTitle(hb_title_fC)
  hb_cut0_fC.SetMinimum(0)
  hb_cut0_fC.SetMaximum(hb_high)
  hb_cut0_fC.SetLineColor(cut0_color)
  hb_cut0_fC.Draw('')

  hb_cut1_fC = fi.Get('hist_hb_totfCinTS_cut5')
  hb_cut1_fC.Scale(10.0 / hb_cut1_fC.GetEntries() )
  hb_cut1_fC.GetXaxis().SetTitle(xaxis)
  hb_cut1_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut1_fC.SetTitle(hb_title_fC)
  hb_cut1_fC.SetLineColor(cut1_color)
  hb_cut1_fC.Draw('same')

  hb_cut2_fC = fi.Get('hist_hb_totfCinTS_cut8')
  hb_cut2_fC.Scale(10.0 / hb_cut2_fC.GetEntries() )
  hb_cut2_fC.GetXaxis().SetTitle(xaxis)
  hb_cut2_fC.GetYaxis().SetTitle(yaxis_fC)
  hb_cut2_fC.SetTitle(hb_title_fC)
  hb_cut2_fC.SetLineColor(cut2_color)
  hb_cut2_fC.Draw('same')

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(hb_cut0_fC, legend_cut0_label, 'l')
  leg.AddEntry(hb_cut1_fC, legend_cut1_label, 'l')
  leg.AddEntry(hb_cut2_fC, legend_cut2_label, 'l')
  leg.Draw('same')

  c.SaveAs("hb_avgfC"+run_num+".png")


# average charge replacement plots
#if True:
if False:
  xaxis = 'TS'
  yaxis_ADC = 'avg ADC'
  yaxis_fC = 'avg fC'
  title_ADC = run_string+'averge ADC per TS in pulse'
  title_fC = run_string+'averge fC per TS in pulse'
  ADC_high = 20.0
  fC_high = 5.0
  legend_title = ''
  legend_xi = 0.7
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.8
  legend_good_label = 'All good hits in HO'
  legend_bad_label = 'Bad hits'
  good_color = kBlack
  bad_color = kRed

  good_ADC = fi.Get('hist_ho_totADCinTS_allgood')
  bad1_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_41_bad')
  bad2_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_42_bad')
  bad3_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_43_bad')
  bad_ADC = bad1_ADC.Clone()
  bad_ADC.Add(bad2_ADC)
  bad_ADC.Add(bad3_ADC)

  good_ADC.Scale(10.0 / good_ADC.GetEntries() )
  bad_ADC.Scale(10.0 / bad_ADC.GetEntries() )
  good_ADC.SetMinimum(0)
  good_ADC.SetMaximum(ADC_high)
  good_ADC.SetLineColor(good_color)
  bad_ADC.SetLineColor(bad_color)

  good_ADC.GetXaxis().SetTitle(xaxis)
  good_ADC.GetYaxis().SetTitle(yaxis_ADC)
  good_ADC.SetTitle(title_ADC)

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good_ADC, legend_good_label, 'l')
  leg.AddEntry(bad_ADC, legend_bad_label, 'l')

  good_ADC.Draw()
  bad_ADC.Draw('same')
  leg.Draw('same')

  c.SaveAs("replacement_avgADC"+run_num+".png")

  good_fC = fi.Get('hist_ho_totfCinTS_allgood')
  bad1_fC = fi.Get('hist_ho_totfCinTS_nocut_12_41_bad')
  bad2_fC = fi.Get('hist_ho_totfCinTS_nocut_12_42_bad')
  bad3_fC = fi.Get('hist_ho_totfCinTS_nocut_12_43_bad')
  bad_fC = bad1_fC.Clone()
  bad_fC.Add(bad2_fC)
  bad_fC.Add(bad3_fC)

  good_fC.Scale(10.0 / good_fC.GetEntries() )
  bad_fC.Scale(10.0 / bad_fC.GetEntries() )
  good_fC.SetMinimum(0)
  good_fC.SetMaximum(fC_high)
  good_fC.SetLineColor(good_color)
  bad_fC.SetLineColor(bad_color)

  good_fC.GetXaxis().SetTitle(xaxis)
  good_fC.GetYaxis().SetTitle(yaxis_fC)
  good_fC.SetTitle(title_fC)

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good_fC, legend_good_label, 'l')
  leg.AddEntry(bad_fC, legend_bad_label, 'l')

  good_fC.Draw()
  bad_fC.Draw('same')
  leg.Draw('same')

  c.SaveAs("replacement_avgfC"+run_num+".png")

# good vs bad only
if True:
#if False:
  xaxis = 'TS'
  yaxis_ADC = 'avg ADC'
  yaxis_fC = 'avg fC'
  title_ADC = run_string+'averge ADC per TS in pulse'
  title_fC = run_string+'averge fC per TS in pulse'
  ADC_high = 20.0
  fC_high = 5.0
  legend_title = ''
  legend_xi = 0.7
  legend_xf = 0.9
  legend_yi = 0.7
  legend_yf = 0.8
  legend_good_label = 'Good hits in faulty channels'
  legend_bad_label = 'Bad hits in faulty channels'
  good_color = kBlack
  bad_color = kRed

  good1_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_41_good')
  good2_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_42_good')
  good3_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_43_good')
  good_ADC = good1_ADC.Clone()
  good_ADC.Add(good2_ADC)
  good_ADC.Add(good3_ADC)

  bad1_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_41_bad')
  bad2_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_42_bad')
  bad3_ADC = fi.Get('hist_ho_totADCinTS_nocut_12_43_bad')
  bad_ADC = bad1_ADC.Clone()
  bad_ADC.Add(bad2_ADC)
  bad_ADC.Add(bad3_ADC)

  good_ADC.Scale(10.0 / good_ADC.GetEntries() )
  bad_ADC.Scale(10.0 / bad_ADC.GetEntries() )
  good_ADC.SetMinimum(0)
  good_ADC.SetMaximum(ADC_high)
  good_ADC.SetLineColor(good_color)
  bad_ADC.SetLineColor(bad_color)

  good_ADC.GetXaxis().SetTitle(xaxis)
  good_ADC.GetYaxis().SetTitle(yaxis_ADC)
  good_ADC.SetTitle(title_ADC)

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good_ADC, legend_good_label, 'l')
  leg.AddEntry(bad_ADC, legend_bad_label, 'l')

  good_ADC.Draw()
  bad_ADC.Draw('same')
  leg.Draw('same')

  c.SaveAs("goodvsbad_faulty_avgADC"+run_num+".png")

  good1_fC = fi.Get('hist_ho_totfCinTS_nocut_12_41_good')
  good2_fC = fi.Get('hist_ho_totfCinTS_nocut_12_42_good')
  good3_fC = fi.Get('hist_ho_totfCinTS_nocut_12_43_good')
  good_fC = good1_fC.Clone()
  good_fC.Add(good2_fC)
  good_fC.Add(good3_fC)

  bad1_fC = fi.Get('hist_ho_totfCinTS_nocut_12_41_bad')
  bad2_fC = fi.Get('hist_ho_totfCinTS_nocut_12_42_bad')
  bad3_fC = fi.Get('hist_ho_totfCinTS_nocut_12_43_bad')
  bad_fC = bad1_fC.Clone()
  bad_fC.Add(bad2_fC)
  bad_fC.Add(bad3_fC)

  good_fC.Scale(10.0 / good_fC.GetEntries() )
  bad_fC.Scale(10.0 / bad_fC.GetEntries() )
  good_fC.SetMinimum(0)
  good_fC.SetMaximum(fC_high)
  good_fC.SetLineColor(good_color)
  bad_fC.SetLineColor(bad_color)

  good_fC.GetXaxis().SetTitle(xaxis)
  good_fC.GetYaxis().SetTitle(yaxis_fC)
  good_fC.SetTitle(title_fC)

  leg = TLegend(legend_xi, legend_yi, legend_xf, legend_yf, legend_title)
  leg.AddEntry(good_fC, legend_good_label, 'l')
  leg.AddEntry(bad_fC, legend_bad_label, 'l')

  good_fC.Draw()
  bad_fC.Draw('same')
  leg.Draw('same')

  c.SaveAs("goodvsbad_faulty_avgfC"+run_num+".png")

