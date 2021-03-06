

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak6CaloJets"),
    matched = cms.InputTag("ak6HiGenJets")
    )

ak6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("ak6CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

ak6Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("ak6CaloJets"),
    payload = "AK6Calo_HI"
    )

ak6CalopatJets = patJets.clone(jetSource = cms.InputTag("ak6CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6Calocorr")),
                                               genJetMatch = cms.InputTag("ak6Calomatch"),
                                               genPartonMatch = cms.InputTag("ak6Caloparton"),
                                               jetIDMap = cms.InputTag("ak6CaloJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = False,
                                               addGenJetMatch      = False,
                                               embedGenJetMatch    = False,
                                               embedGenPartonMatch = False,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

ak6CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak6CalopatJets"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.6,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator")
                                                             )

ak6CaloJetSequence_mc = cms.Sequence(
						  ak6Calomatch
                                                  *
                                                  ak6Caloparton
                                                  *
                                                  ak6Calocorr
                                                  *
                                                  ak6CalopatJets
                                                  *
                                                  ak6CaloJetAnalyzer
                                                  )

ak6CaloJetSequence_data = cms.Sequence(ak6Calocorr
                                                    *
                                                    ak6CalopatJets
                                                    *
                                                    ak6CaloJetAnalyzer
                                                    )

ak6CaloJetSequence_jec = ak6CaloJetSequence_mc
ak6CaloJetSequence_mix = ak6CaloJetSequence_mc

ak6CaloJetSequence = cms.Sequence(ak6CaloJetSequence_data)
