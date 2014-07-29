#include <TFile.h>
#include <TCanvas.h>
#include <TTree.h>
#include <TLegend.h>
#include <TH1D.h>
#include <TProfile.h>

void plot2() {
   TFile *a = new TFile("PythiaZ2Star.root");
   TFile *b = new TFile("jewel-80-mpt.root");
   TFile *c = new TFile("Pyquen.root");
   TFile *d = new TFile("PyquenWide.root");
   TTree *ta = (TTree*)a->Get("dijet/nt");
   TTree *tb = (TTree*)b->Get("dijet/nt");   
   TTree *tc = (TTree*)c->Get("dijet/nt");
   TTree *td = (TTree*)d->Get("dijet/nt");
   
   TCanvas *c1 = new TCanvas("c1","",600,600);
   
   TProfile *ha = new TProfile("ha","",20,100,300);
   TProfile *hb = new TProfile("hb","",20,100,300);
   TProfile *hc = new TProfile("hc","",20,100,300);
   TProfile *hd = new TProfile("hd","",20,100,300);
   ta->Draw("(pt1-pt2)/(pt1+pt2):pt1>>ha","pt1>100&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
   tb->Draw("(pt1-pt2)/(pt1+pt2):pt1>>hb","pt1>100&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
   tc->Draw("(pt1-pt2)/(pt1+pt2):pt1>>hc","pt1>100&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
   td->Draw("(pt1-pt2)/(pt1+pt2):pt1>>hd","pt1>100&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
//   ta->Draw("pt2/pt1>>ha","pt1>120&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
//   tb->Draw("pt2/pt1>>hb","pt1>120&&pt2>30&&acos(cos(dphi))>2/3.*3.14159");
   
   hb->SetMarkerColor(2);
   hb->SetLineColor(2);
   hc->SetMarkerColor(4);
   hc->SetLineColor(4);
   hd->SetLineColor(kGreen+1);
   hd->SetMarkerColor(kGreen+1);
   ha->Draw();
   int na=ha->GetEntries();
//   ha->Scale(1./na);
//   hb->Sumw2();
   int nb=hb->GetEntries();
//   hb->Scale(1./nb);
   hb->SetMarkerStyle(2);
   hb->SetMarkerStyle(20);
//   hc->Sumw2();
   int nc=hc->GetEntries();
//   hc->Scale(1./nc);
   hc->SetMarkerStyle(2);
   hc->SetMarkerStyle(20);
//   hd->Sumw2();
   int nd=hd->GetEntries();
//   hd->Scale(1./nd);
   hd->SetMarkerStyle(2);
   hd->SetMarkerStyle(20);

   ha->SetXTitle("A_{J}");
   ha->SetYTitle("Event Fraction");
   ha->Draw();
   hb->Draw("same");
   hc->Draw("same");
   hd->Draw("same");

   TLegend *leg = new TLegend(0.4,0.5,0.9,0.9);
   leg->SetFillStyle(0);
   leg->SetBorderSize(0);
   leg->Draw();
   leg->AddEntry(ha,"p_{T,1} > 100 GeV, p_{T,2} > 30 GeV","");
   leg->AddEntry(ha,"#Delta#phi>2#pi/3","");
   leg->AddEntry(ha,"PYTHIA Z2* GEN","l");
   leg->AddEntry(hb,"JEWEL GEN","pl");
   leg->AddEntry(hc,"PYQUEN GEN","pl");
   leg->AddEntry(hd,"PYQUEN Wide GEN","pl");
   leg->Draw();
   
}
