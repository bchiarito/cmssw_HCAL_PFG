#define tree_cxx
#include "tree.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

#include <iostream>
#include <chrono>

using namespace std::chrono;
using std::cout;
using std::endl;

void do_analysis()
{
  TChain* chain = new TChain("hcalTupleTree/tree");
  chain->Add("HcalTupleMaker_new2_5k.root");

  tree* analysis = new tree(chain);
  analysis->Loop();
}

void tree::Loop()
{
//   In a ROOT session, you can do:
//      root> .L tree.C
//      root> tree t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   // make output file
   TFile * outfile = new TFile("loop_histos.root", "RECREATE");
   outfile->cd();

   // book histos
   TH1F* num_hits_ho = new TH1F("num_hits_ho","num_hits_ho",1000,0,10000);
   TH1F* num_hits_he = new TH1F("num_hits_he","num_hits_he",1000,0,10000);
   TH1F* num_hits_hb = new TH1F("num_hits_hb","num_hits_hb",1000,0,10000);
   TH1F* num_hits_hf = new TH1F("num_hits_hf","num_hits_hf",10000,0,10000);

   TH1F* capid_0_ho = new TH1F("capid_0_ho","capid_0_ho",8,0,4);
   TH1F* capid_0_he = new TH1F("capid_0_he","capid_0_he",8,0,4);
   TH1F* capid_0_hb = new TH1F("capid_0_hb","capid_0_hb",8,0,4);
   TH1F* capid_0_hf = new TH1F("capid_0_hf","capid_0_hf",8,0,4);

   TH1F* capid_soi_he = new TH1F("capid_soi_he","capid_soi_he",8,0,4);
   TH1F* capid_soi_hf = new TH1F("capid_soi_hf","capid_soi_hf",8,0,4);

   TH1F* soi_he = new TH1F("soi_he","soi_he",20,0,10);
   TH1F* soi_hf = new TH1F("soi_hf","soi_hf",20,0,10);

   TH1F* capid_0_bx_mod4_ho = new TH1F("capid_0_bx_mod4_ho","capid_0_bx_mod4_ho",8,0,4);
   TH1F* capid_0_bx_mod4_he = new TH1F("capid_0_bx_mod4_he","capid_0_bx_mod4_he",8,0,4);
   TH1F* capid_0_bx_mod4_hb = new TH1F("capid_0_bx_mod4_hb","capid_0_bx_mod4_hb",8,0,4);
   TH1F* capid_0_bx_mod4_hf = new TH1F("capid_0_bx_mod4_hf","capid_0_bx_mod4_hf",8,0,4);

   TH1F* capid_soi_bx_mod4_he = new TH1F("capid_soi_bx_mod4_he","capid_soi_bx_mod4_he",8,0,4);
   TH1F* capid_soi_bx_mod4_hf = new TH1F("capid_soi_bx_mod4_hf","capid_soi_bx_mod4_hf",8,0,4);
   TH1F* capid_effsoi_bx_mod4_ho = new TH1F("capid_effsoi_bx_mod4_ho","capid_effsoi_bx_mod4_ho",8,0,4);
   TH1F* capid_effsoi_bx_mod4_hb = new TH1F("capid_effsoi_bx_mod4_hb","capid_effsoi_bx_mod4_hb",8,0,4);

   TH1F* num_bad_rotations = new TH1F("num_bad_rotations","num_bad_rotations",1000,0,1000);
   TH1F* num_good_rotations = new TH1F("num_good_rotations","num_good_rotations",1000,0,1000);
   TH1F* frac_bad_rotations = new TH1F("frac_bad_rotations","frac_bad_rotations",1000,0,1);

   TH1F* tot_perhit_charge = new TH1F("tot_perhit_charge","tot_perhit_charge",200,0,60);
   TH1F* tot_bad_perhit_charge = new TH1F("tot_bad_perhit_charge","tot_bad_perhit_charge",200,0,60);

   TH1F* avg_ts_charge = new TH1F("avg_ts_charge","avg_ts_charge",12,0,12);
   TH1F* avg_ts_charge_bad = new TH1F("avg_ts_charge_bad","avg_ts_charge_bad",12,0,12);

   // constants
   const int FIRST_HO_TS = 2;
   const int LAST_HO_TS = 5;

   // event loop
   std::cout << "starting loop" << std::endl;
   high_resolution_clock::time_point t1 = high_resolution_clock::now();
   Long64_t nentries = fChain->GetEntriesFast();
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      if (jentry % 100 == 0) {
        std::cout << "processing entry " << jentry << std::endl;
      }
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      fChain->GetEntry(jentry);
      
      num_hits_ho->Fill(HODigiCapID->size());
      num_hits_he->Fill(QIE11DigiCapID->size());
      num_hits_hb->Fill(HBHEDigiCapID->size());
      num_hits_hf->Fill(QIE10DigiCapID->size());

      for (unsigned int i = 0; i < HODigiCapID->size(); i++) { capid_0_ho->Fill( (*HODigiCapID)[i][0] ); }
      for (unsigned int i = 0; i < QIE11DigiCapID->size(); i++) { capid_0_he->Fill( (*QIE11DigiCapID)[i][0] ); }
      for (unsigned int i = 0; i < HBHEDigiCapID->size(); i++) { capid_0_hb->Fill( (*HBHEDigiCapID)[i][0] ); }
      for (unsigned int i = 0; i < QIE10DigiCapID->size(); i++) { capid_0_hf->Fill( (*QIE10DigiCapID)[i][0] ); }

      for (unsigned int i = 0; i < QIE11DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE11DigiCapID)[i].size(); ii++) {
          if ( (*QIE11DigiSOI)[i][ii] == 1 )
            capid_soi_he->Fill( (*QIE11DigiCapID)[i][ii] );
        }
      }

      for (unsigned int i = 0; i < QIE11DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE11DigiCapID)[i].size(); ii++) {
          if ( (*QIE11DigiSOI)[i][ii] == 1 )
            soi_he->Fill( ii );
        }
      }

      for (unsigned int i = 0; i < QIE10DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE10DigiCapID)[i].size(); ii++) {
          if ( (*QIE10DigiSOI)[i][ii] == 1 )
            capid_soi_hf->Fill( (*QIE10DigiCapID)[i][ii] );
        }
      }

      for (unsigned int i = 0; i < QIE10DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE10DigiCapID)[i].size(); ii++) {
          if ( (*QIE10DigiSOI)[i][ii] == 1 )
            soi_hf->Fill( ii );
        }
      }

      for (unsigned int i = 0; i < HODigiCapID->size(); i++) { capid_0_bx_mod4_ho->Fill( ((*HODigiCapID)[i][0] - bx) % 4); }
      for (unsigned int i = 0; i < QIE11DigiCapID->size(); i++) { capid_0_bx_mod4_he->Fill( ((*QIE11DigiCapID)[i][0] - bx) % 4); }
      for (unsigned int i = 0; i < HBHEDigiCapID->size(); i++) { capid_0_bx_mod4_hb->Fill( ((*HBHEDigiCapID)[i][0] - bx) % 4); }
      for (unsigned int i = 0; i < QIE10DigiCapID->size(); i++) { capid_0_bx_mod4_hf->Fill( ((*QIE10DigiCapID)[i][0] - bx) % 4); }

      for (unsigned int i = 0; i < QIE11DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE11DigiCapID)[i].size(); ii++) {
          if ( (*QIE11DigiSOI)[i][ii] == 1 )
            capid_soi_bx_mod4_he->Fill( ((*QIE11DigiCapID)[i][ii] - bx) % 4);
        }
      }

      for (unsigned int i = 0; i < QIE10DigiCapID->size(); i++) {
        for (unsigned int ii = 0; ii < (*QIE10DigiCapID)[i].size(); ii++) {
          if ( (*QIE10DigiSOI)[i][ii] == 1 )
            capid_soi_bx_mod4_hf->Fill( ((*QIE10DigiCapID)[i][ii] - bx) % 4);
        }
      }

      for (unsigned int i = 0; i < HODigiCapID->size(); i++) { capid_effsoi_bx_mod4_ho->Fill( ((*HODigiCapID)[i][4] - bx) % 4); }
      for (unsigned int i = 0; i < HBHEDigiCapID->size(); i++) { capid_effsoi_bx_mod4_hb->Fill( ((*HBHEDigiCapID)[i][3] - bx) % 4); }

      float ev_num_bad_rotations = 0;
      for (unsigned int i = 0; i < HODigiCapID->size(); i++) {
        if( (((*HODigiCapID)[i][4] - bx) % 4) != 1 ) ev_num_bad_rotations += 1;
      }
      num_bad_rotations->Fill(ev_num_bad_rotations);

      float ev_num_good_rotations = 0;
      for (unsigned int i = 0; i < HODigiCapID->size(); i++) {
        if( (((*HODigiCapID)[i][4] - bx) % 4) == 1 ) ev_num_good_rotations += 1;
      }
      num_good_rotations->Fill(ev_num_good_rotations);

      float ev_frac_bad_rotations = ev_num_bad_rotations / (ev_num_bad_rotations + ev_num_good_rotations);
      frac_bad_rotations->Fill(ev_frac_bad_rotations);

      for (unsigned int i = 0; i < HODigiCapID->size(); i++) {
        float total_charge = 0;
        for (unsigned int ii = 0; ii < (*HODigiCapID)[i].size(); ii++) {
          if (ii >= FIRST_HO_TS && ii <= LAST_HO_TS) total_charge += (*HODigiFC)[i][ii];
        }
        tot_perhit_charge->Fill(total_charge);
      }

      for (unsigned int i = 0; i < HODigiCapID->size(); i++) {
        if( (((*HODigiCapID)[i][4] - bx) % 4) == 1 ) continue;
        float total_charge = 0;
        for (unsigned int ii = 0; ii < (*HODigiCapID)[i].size(); ii++) {
          if (ii >= FIRST_HO_TS && ii <= LAST_HO_TS) total_charge += (*HODigiFC)[i][ii];
        }
        tot_bad_perhit_charge->Fill(total_charge);
      }

   }
   std::cout << "done loop" << std::endl;
   high_resolution_clock::time_point t2 = high_resolution_clock::now();
   auto duration = duration_cast<seconds>( t2 - t1 ).count();
   std::cout << duration << " seconds" << std::endl;

   // draw histos

   // save histos
   outfile->Write();
}
