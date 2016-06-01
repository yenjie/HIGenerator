#!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

hiTrackQuality = "highPurity"              # iterative tracks
#hiTrackQuality = "highPuritySetWithPV"    # calo-matched tracks

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
                            "file:/afs/cern.ch/user/d/dgulhan/workDir/2849B7CC-6B79-E211-B677-002618943962.root"
    ))

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('RecoHI.HiCentralityAlgos.CentralityBin_cfi')

process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V43D::All', '')

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_pp2760(process)
overrideJEC_pp2760(process)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string("HFtowersTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    centralitySrc = cms.InputTag("hiCentrality")
    )

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("/afs/cern.ch/user/d/dgulhan/workDir/trackAnalyzerUpdateOut/HiForest_imppar.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

#process.load('Configuration.StandardSequences.Generator_cff')
#process.load('RecoJets.Configuration.GenJetParticles_cff')
#process.load('RecoHI.HiJetAlgos.HiGenJets_cff')
#process.load('RecoHI.HiJetAlgos.HiRecoJets_cff')
#process.load('RecoHI.HiJetAlgos.HiRecoPFJets_cff')

#process.hiGenParticles.srcVector = cms.vstring('generator')

process.hiCentrality.producePixelhits = False
process.hiCentrality.producePixelTracks = False
process.hiCentrality.srcTracks = cms.InputTag("generalTracks")
process.hiCentrality.srcVertex = cms.InputTag("offlinePrimaryVerticesWithBS")
process.hiEvtPlane.vtxCollection_ = cms.InputTag("offlinePrimaryVerticesWithBS")
process.hiEvtPlane.trackCollection_ = cms.InputTag("generalTracks")

process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiGenJetsCleaned_JEC_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5CaloJetSequence_pp_data_cff')


process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_pp_cff')
process.voronoiBackgroundPF.src = cms.InputTag("particleFlow")
process.PFTowers.src = cms.InputTag("particleFlow")

process.jetSequences = cms.Sequence(process.voronoiBackgroundCalo +
                                    process.voronoiBackgroundPF +
                                    process.PFTowers +
                                    process.hiReRecoCaloJets +
                                    process.hiReRecoPFJets +

                                    process.akPu2CaloJetSequence +
                                    process.akVs2CaloJetSequence +
                                    process.akVs2PFJetSequence +
                                    process.akPu2PFJetSequence +
                                    process.ak2PFJetSequence +
                                    process.ak2CaloJetSequence +

                                    process.akPu3CaloJetSequence +
                                    process.akVs3CaloJetSequence +
                                    process.akVs3PFJetSequence +
                                    process.akPu3PFJetSequence +
                                    process.ak3PFJetSequence +
                                    process.ak3CaloJetSequence +

                                    process.akPu4CaloJetSequence +
                                    process.akVs4CaloJetSequence +
                                    process.akVs4PFJetSequence +
                                    process.akPu4PFJetSequence +
                                    process.ak4PFJetSequence +
                                    process.ak4CaloJetSequence +

                                    process.akPu5CaloJetSequence +
                                    process.akVs5CaloJetSequence +
                                    process.akVs5PFJetSequence +
                                    process.akPu5PFJetSequence +
                                    process.ak5PFJetSequence +
                                    process.ak5CaloJetSequence

                                    )

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
#process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVerticesWithBS")

#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
#process.load('HeavyIonsAnalysis.JetAnalysis.ExtraPfReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_pp_cfi')
process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#####################################################################################

#########################
# Track Analyzer
#########################
process.hiTracks.cut = cms.string('quality("highPurity")')

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = False
process.ppTrack.doPFMatching = False
process.ppTrack.doTrackVtxWImpPar = cms.untracked.bool(True)

                                                       #####################
# photons
process.load('HeavyIonsAnalysis.JetAnalysis.EGammaAnalyzers_cff')
process.photonStep.remove(process.photonMatch)
process.hiGoodTracks.src = cms.InputTag("generalTracks")
process.hiGoodTracks.vertices = cms.InputTag("offlinePrimaryVerticesWithBS")
process.cleanPhotons.primaryVertexProducer = cms.string("offlinePrimaryVerticesWithBS")
process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()

#####################
# muons
######################
process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
process.hltMuTree.doGen = cms.untracked.bool(True)
process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("akVs3PFJets")
process.globalMuons.TrackerCollectionLabel = "generalTracks"
process.muons.TrackExtractorPSet.inputTrackCollection = "generalTracks"
process.muons.inputCollectionLabels = ["generalTracks", "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

process.ana_step = cms.Path(process.hiCentrality +
                            process.centralityBin +
                            process.hiEvtPlane +
                            process.hiEvtAnalyzer*
                            process.jetSequences +
                            process.photonStep +
                            process.pfcandAnalyzer +
                            process.rechitAna +
#temp                            process.hltMuTree +
                            process.HiForest +
                            process.ppTrack)

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.phltJetHI = cms.Path( process.hltJetHI )
#process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
#process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

# Customization
from HeavyIonsAnalysis.JetAnalysis.customise_cfi import *
setPhotonObject(process,"cleanPhotons")

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')

process.hltAna = cms.Path(process.hltanalysis)
process.pAna = cms.EndPath(process.skimanalysis)
