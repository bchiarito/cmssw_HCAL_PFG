from ROOT import *



fi = TFile('summed_output_321005jet.root')

good_41 = fi.Get('hist_ho_totfCinTS_cut20_12_41_good')
good_42 = fi.Get('hist_ho_totfCinTS_cut20_12_42_good')
good_43 = fi.Get('hist_ho_totfCinTS_cut20_12_43_good')
bad_41 = fi.Get('hist_ho_totfCinTS_cut20_12_41_bad')
bad_42 = fi.Get('hist_ho_totfCinTS_cut20_12_42_bad')
bad_43 = fi.Get('hist_ho_totfCinTS_cut20_12_43_bad')

good = good_41.Clone()
good.Add(good_42)
good.Add(good_43)

bad = bad_41.Clone()
bad.Add(bad_42)
bad.Add(bad_43)

good.Scale( 10.0 / good.GetEntries())
bad.Scale( 10.0 / bad.GetEntries())

good.SetTitle('JetHT 321005, one TS with ADC > 20')

bad.SetLineColor(kRed)

leg = TLegend(0.7, 0.7, 0.9, 0.9, '')
leg.AddEntry(good, 'Good hits in iEta 12, iPhi 41,42,43', 'l')
leg.AddEntry(bad, 'Good hits in iEta 12, iPhi 41,42,43', 'l')

good.Draw()
bad.Draw('same')
leg.Draw('same')
raw_input()
