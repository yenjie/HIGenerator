#include <TFile.h>
#include <TCanvas.h>
#include <TTree.h>
#include <TLegend.h>
#include <TH1D.h>
#include <TH2D.h>

void compareQPythia4() {
//   TFile *a = new TFile("PythiaZ2Star.root");
   TFile *a = new TFile("QPythia_PQM0.root");
   TFile *b = new TFile("QPythia_PQM0.root");
   TFile *c = new TFile("QPythia_PQM1.root");
   TFile *d = new TFile("QPythia_PQM1.28.root");
   TFile *e = new TFile("QPythia_PQM4.root");
   TTree *ta = (TTree*)a->Get("dijet/t");
   TTree *tb = (TTree*)b->Get("dijet/t");   
   TTree *tbhi = (TTree*)b->Get("ana/hi");
   TTree *tbnt = (TTree*)b->Get("ana/nt");
   tb->AddFriend(tbhi);
   tb->AddFriend(tbnt);
   TTree *tc = (TTree*)c->Get("dijet/t");
   TTree *td = (TTree*)d->Get("dijet/t");
   TTree *te = (TTree*)e->Get("dijet/t");
   
   
   TCanvas *c1 = new TCanvas("c1","",600,600);
   
   TH2D *h0 = new TH2D("h0","",20,100,300,2000,0,2);
   TH1D *ha = new TH1D("ha","",20,100,300);
   TH1D *hb = new TH1D("hb","",20,100,300);
   TH1D *hc = new TH1D("hc","",20,100,300);
   TH1D *hd = new TH1D("hd","",20,100,300);
   TH1D *he = new TH1D("he","",20,100,300);
   ta->Draw("jtpt>>ha","");
   tb->Draw("jtpt>>hb","b<0.05");
   tc->Draw("jtpt>>hc","");
   td->Draw("jtpt>>hd","");
   te->Draw("jtpt>>he","");
//   ta->Draw("pt2/pt1>>ha","");
//   tb->Draw("pt2/pt1>>hb","");


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
   hb->SetMarkerStyle(2);
   hb->SetMarkerStyle(20);
   hc->SetMarkerStyle(2);
   hc->SetMarkerStyle(20);
   hd->SetMarkerStyle(2);
   hd->SetMarkerStyle(20);
   he->SetMarkerStyle(2);
   he->SetMarkerStyle(20);

   h0->SetXTitle("Jet p_{T} (GeV/c)");
   h0->SetYTitle("R_{AA}");
//   h0->SetMaximum(0.5)  
//   ha->SetFillStyle(3001);
//   ha->SetFillColor(kGray);
   ha->Sumw2();
   hb->Sumw2();
   hc->Sumw2();
   hd->Sumw2();
   he->Sumw2();
   ha->Scale(1./ta->GetEntries());
   hb->Scale(1./tb->GetEntries("b<0.05"));
   hc->Scale(1./tc->GetEntries());
   hd->Scale(1./td->GetEntries());
   he->Scale(1./te->GetEntries());

   h0->Draw("hist");
   hb->Divide(ha);
   hc->Divide(ha);
   hd->Divide(ha);
   he->Divide(ha);
   ha->Divide(ha);
   ha->Draw("hist same");
   hb->Draw("hist c same");
   hc->Draw("hist c same");
   hd->Draw("hist c same");
   he->Draw("hist c same");
   hb->Draw("same");
   hc->Draw("same");
   hd->Draw("same");
   he->Draw("same");

   TLegend *leg = new TLegend(0.4,0.6,0.9,0.9);
   leg->SetFillStyle(0);
   leg->SetBorderSize(0);
   leg->Draw();
   leg->AddEntry(ha,"Leading Jet p_{T}> 100 GeV","");
   leg->AddEntry(ha,"Jet p_{T}> 30 GeV","");
   leg->AddEntry(ha,"PYTHIA Z2* GEN","l");
   leg->AddEntry(hb,"QPYTHIA PQM0 GEN","l");
   leg->AddEntry(hc,"QPYTHIA PQM1 GEN","l");
   leg->AddEntry(hd,"QPYTHIA PQM1.28 GEN","l");
   leg->AddEntry(he,"QPYTHIA PQM4 GEN","l");

   leg->Draw();
   
}
