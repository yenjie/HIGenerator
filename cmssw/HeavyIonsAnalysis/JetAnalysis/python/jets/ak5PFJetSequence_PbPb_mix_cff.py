

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak5PFJets"),
    matched = cms.InputTag("ak5HiGenJetsCleaned")
    )

ak5PFparton = patJetPartonMatch.clone(src = cms.InputTag("ak5PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

ak5PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("ak5PFJets"),
    payload = "AK5PF_hiIterativeTracks"
    )

ak5PFpatJets = patJets.clone(jetSource = cms.InputTag("ak5PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5PFcorr")),
                                               genJetMatch = cms.InputTag("ak5PFmatch"),
                                               genPartonMatch = cms.InputTag("ak5PFparton"),
                                               jetIDMap = cms.InputTag("ak5PFJetID"),
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

ak5PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak5PFpatJets"),
                                                             genjetTag = 'ak5HiGenJetsCleaned',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs5PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles"),
							     eventInfoTag = cms.InputTag("hiSignal")
                                                             )

ak5PFJetSequence_mc = cms.Sequence(
						  ak5PFmatch
                                                  *
                                                  ak5PFparton
                                                  *
                                                  ak5PFcorr
                                                  *
                                                  ak5PFpatJets
                                                  *
                                                  ak5PFJetAnalyzer
                                                  )

ak5PFJetSequence_data = cms.Sequence(ak5PFcorr
                                                    *
                                                    ak5PFpatJets
                                                    *
                                                    ak5PFJetAnalyzer
                                                    )

ak5PFJetSequence_jec = ak5PFJetSequence_mc
ak5PFJetSequence_mix = ak5PFJetSequence_mc

ak5PFJetSequence = cms.Sequence(ak5PFJetSequence_mix)
