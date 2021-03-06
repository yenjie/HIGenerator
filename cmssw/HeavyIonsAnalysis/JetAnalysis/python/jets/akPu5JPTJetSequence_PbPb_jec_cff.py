

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.JPTJetAnalyzer_cff import *

#Parameters for JPT RECO jets in PbPb

from RecoJets.JetPlusTracks.JetPlusTrackCorrectionsAA_cff import *
tracks = cms.InputTag("hiGeneralTracks")

from RecoJets.JetAssociationProducers.trackExtrapolator_cfi import *
trackExtrapolator.trackSrc = cms.InputTag("hiGeneralTracks")

from RecoJets.JetAssociationProducers.iterativeCone5JTA_cff import*
JPTAntiKtPu5JetTracksAssociatorAtVertex.tracks = cms.InputTag("hiGeneralTracks")

from RecoJets.JetPlusTracks.JetPlusTrackCorrectionsAA_cff import *
JetPlusTrackZSPCorJetAntiKtPu5.tracks = cms.InputTag("hiGeneralTracks")
JetPlusTrackZSPCorJetAntiKtPu5.EfficiencyMap = cms.string("HeavyIonsAnalysis/JetAnalysis/python/jets/CMSSW_538HI_TrackNonEff.txt")

from RecoJets.JetAssociationProducers.ak5JTA_cff import*
JPTAntiKtPu5JetTracksAssociatorAtVertex = ak5JetTracksAssociatorAtVertex.clone()
JPTAntiKtPu5JetTracksAssociatorAtVertex.jets = cms.InputTag("akPu5CaloJets")
JPTAntiKtPu5JetTracksAssociatorAtVertex.tracks = cms.InputTag("hiGeneralTracks")

JPTAntiKtPu5JetTracksAssociatorAtCaloFace = ak5JetTracksAssociatorAtCaloFace.clone()
JPTAntiKtPu5JetTracksAssociatorAtCaloFace.jets = cms.InputTag("akPu5CaloJets")
JPTAntiKtPu5JetTracksAssociatorAtCaloFace.tracks = cms.InputTag("hiGeneralTracks")

JPTAntiKtPu5JetExtender.jets = cms.InputTag("akPu5CaloJets")
JPTAntiKtPu5JetExtender.jet2TracksAtCALO = cms.InputTag("JPTAntiKtPu5JetTracksAssociatorAtCaloFace")
JPTAntiKtPu5JetExtender.jet2TracksAtVX = cms.InputTag("JPTAntiKtPu5JetTracksAssociatorAtVertex")

from RecoJets.JetPlusTracks.JetPlusTrackCorrectionsAA_cff import *
#define jetPlusTrackZSPCorJet sequences
jetPlusTrackZSPCorJetIconePu5   = cms.Sequence(JetPlusTrackCorrectionsIconePu5)
jetPlusTrackZSPCorJetSisconePu5 = cms.Sequence(JetPlusTrackCorrectionsSisConePu5)
jetPlusTrackZSPCorJetAntiKtPu5  = cms.Sequence(JetPlusTrackCorrectionsAntiKtPu5)

recoJPTJetsHIC=cms.Sequence(jetPlusTrackZSPCorJetAntiKtPu5)


akPu5JPTmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
    matched = cms.InputTag("ak5HiGenJetsCleaned")
    )

akPu5JPTparton = patJetPartonMatch.clone(src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu5JPTcorr = patJetCorrFactors.clone(
    useNPV = True,
    primaryVertices = cms.InputTag("hiSelectedVertex"),
   # levels   = cms.vstring('L1Offset','L1JPTOffset','L2Relative','L3Absolute'),
    levels   = cms.vstring('L1Offset'),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
    payload = "AK5JPT",
#    extraJPTOffset = cms.string("L1Offset")
    )

akPu5JPTpatJets = patJets.clone(
                                               jetSource = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5JPTcorr")),
                                               genJetMatch = cms.InputTag("akPu5JPTmatch"),
                                               genPartonMatch = cms.InputTag("akPu5JPTparton"),
                                               jetIDMap = cms.InputTag("ak5CaloJetID"),
					       addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True, 
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

akPu5JPTJetAnalyzer = JPTJetAnalyzer.clone(jetTag = cms.InputTag("akPu5JPTpatJets"),
                                                             genjetTag = 'ak5HiGenJetsCleaned',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )

akPu5JPTJetSequence_mc = cms.Sequence(
						  akPu5JPTmatch
                                                  *
                                                  akPu5JPTparton
                                                  *
                                                  akPu5JPTcorr
                                                  *
                                                  akPu5JPTpatJets
                                                  *
                                                  akPu5JPTJetAnalyzer
                                                  )

akPu5JPTJetSequence_data = cms.Sequence(
						    akPu5JPTcorr
                                                    *
                                                    akPu5JPTpatJets
                                                    *
                                                    akPu5JPTJetAnalyzer
                                                    )

akPu5JPTJetSequence_jec = akPu5JPTJetSequence_mc
akPu5JPTJetSequence = cms.Sequence(akPu5JPTJetSequence_jec)
akPu5JPTJetAnalyzer.genPtMin = cms.untracked.double(1)

