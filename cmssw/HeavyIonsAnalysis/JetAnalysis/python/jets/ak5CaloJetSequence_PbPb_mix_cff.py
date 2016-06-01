

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak5CaloJets"),
    matched = cms.InputTag("ak5HiGenJetsCleaned")
    )

ak5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("ak5CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

ak5Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("ak5CaloJets"),
    payload = "AK5Calo_HI"
    )

ak5CalopatJets = patJets.clone(jetSource = cms.InputTag("ak5CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5Calocorr")),
                                               genJetMatch = cms.InputTag("ak5Calomatch"),
                                               genPartonMatch = cms.InputTag("ak5Caloparton"),
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

ak5CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak5CalopatJets"),
                                                             genjetTag = 'ak5HiGenJetsCleaned',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles"),
							     eventInfoTag = cms.InputTag("hiSignal")
                                                             )

ak5CaloJetSequence_mc = cms.Sequence(
						  ak5Calomatch
                                                  *
                                                  ak5Caloparton
                                                  *
                                                  ak5Calocorr
                                                  *
                                                  ak5CalopatJets
                                                  *
                                                  ak5CaloJetAnalyzer
                                                  )

ak5CaloJetSequence_data = cms.Sequence(ak5Calocorr
                                                    *
                                                    ak5CalopatJets
                                                    *
                                                    ak5CaloJetAnalyzer
                                                    )

ak5CaloJetSequence_jec = ak5CaloJetSequence_mc
ak5CaloJetSequence_mix = ak5CaloJetSequence_mc

ak5CaloJetSequence = cms.Sequence(ak5CaloJetSequence_mix)
