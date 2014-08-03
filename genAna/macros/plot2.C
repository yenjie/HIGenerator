#include <TFile.h>
#include <TCanvas.h>
#include <TTree.h>
#include <TLegend.h>
#include <TH1D.h>
#include <TH2D.h>

void plot2() {
   TFile *a = new TFile("PythiaZ2Star.root");
   TFile *b = new TFile("jewel-80-mb.root");
//   TFile *b = new TFile("treefileR6.root");
   TFile *c = new TFile("yajem.root");
   TFile *d = new TFile("PyquenWide.root");
   TFile *e = new TFile("test2.root");
   TTree *ta = (TTree*)a->Get("dijet/nt");
   TTree *tb = (TTree*)b->Get("dijet/nt");   
   TTree *tbhi = (TTree*)b->Get("ana/hi");
   TTree *tbnt = (TTree*)b->Get("ana/nt");
   tb->AddFriend(tbhi);
   tb->AddFriend(tbnt);
   TTree *tc = (TTree*)c->Get("dijet/nt");
   TTree *td = (TTree*)d->Get("dijet/nt");
   TTree *te = (TTree*)e->Get("dijet/nt");
   
   
   TCanvas *c1 = new TCanvas("c1","",600,600);
   
   TH2D *h0 = new TH2D("h0","",20,3.14159/2,3.1416,2000,0,1);
   TH1D *ha = new TH1D("ha","",20,3.14159/2,3.1416);
   TH1D *hb = new TH1D("hb","",20,3.14159/2,3.1416);
   TH1D *hc = new TH1D("hc","",20,3.14159/2,3.1416);
   TH1D *hd = new TH1D("hd","",20,3.14159/2,3.1416);
   TH1D *he = new TH1D("he","",20,3.14159/2,3.1416);
   ta->Draw("acos(cos(dphi))>>ha","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");
   tb->Draw("acos(cos(dphi))>>hb","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159&&b<0.05");
   tc->Draw("acos(cos(dphi))>>hc","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");
   td->Draw("acos(cos(dphi))>>hd","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");
   te->Draw("acos(cos(dphi))>>he","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");
//   ta->Draw("pt2/pt1>>ha","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");
//   tb->Draw("pt2/pt1>>hb","pt1>100&&pt2>30&&acos(cos(dphi))>0.5*3.14159");


   hb->SetMarkerColor(2);
   hb->SetLineColor(2);
   hc->SetMarkerColor(4);
   hc->SetLineColor(4);
   hd->SetLineColor(kGreen+1);
   hd->SetMarkerColor(kGreen+1);
   he->SetLineColor(6);
   he->SetMarkerColor(6);
   ha->SetMaximum(0.3);
   ha->Draw();
   int na=ha->GetEntries();
   ha->Scale(1./na);
   hb->Sumw2();
   int nb=hb->GetEntries();
   hb->Scale(1./nb);
   hb->SetMarkerStyle(2);
   hb->SetMarkerStyle(20);
   hc->Sumw2();
   int nc=hc->GetEntries();
   hc->Scale(1./nc);
   hc->SetMarkerStyle(2);
   hc->SetMarkerStyle(20);
   hd->Sumw2();
   int nd=hd->GetEntries();
   hd->Scale(1./nd);
   hd->SetMarkerStyle(2);
   hd->SetMarkerStyle(20);
   int ne=he->GetEntries();
   he->Sumw2();
   he->Scale(1./ne);
   he->SetMarkerStyle(2);
   he->SetMarkerStyle(20);

   h0->SetXTitle("#Delta#phi");
   h0->SetYTitle("Event Fraction");
//   h0->SetMaximum(0.5)  
   h0->Draw();
   ha->SetFillStyle(3001);
   ha->SetFillColor(kGray);
   ha->Draw("same");
   hb->Draw("same");
   hc->Draw("same");
   hd->Draw("same");
   he->Draw("same");

   TLegend *leg = new TLegend(0.4,0.5,0.9,0.9);
   leg->SetFillStyle(0);
   leg->SetBorderSize(0);
   leg->Draw();
   leg->AddEntry(ha,"p_{T,1} > 100 GeV, p_{T,2} > 30 GeV","");
   leg->AddEntry(ha,"#Delta#phi>2#pi/3","");
   leg->AddEntry(ha,"PYTHIA Z2* GEN","l");
   leg->AddEntry(hb,"JEWEL 0-5% GEN","pl");
   leg->AddEntry(hc,"YAJEM d#bar{d} GEN","pl");
   leg->AddEntry(hd,"PYQUEN Wide GEN","pl");
   leg->AddEntry(he,"QPYTHIA 0-5% GEN","pl");

   leg->Draw();
   
}
