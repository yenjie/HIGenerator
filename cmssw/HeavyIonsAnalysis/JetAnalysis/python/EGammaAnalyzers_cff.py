import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.PhotonAnalysis.MultiPhotonAnalyzer_cfi import *
multiPhotonAnalyzer.GenParticleProducer = cms.InputTag("hiGenParticles")
multiPhotonAnalyzer.PhotonProducer = cms.InputTag("selectedPatPhotons")
multiPhotonAnalyzer.VertexProducer = cms.InputTag("hiSelectedVertex")
multiPhotonAnalyzer.OutputFile = cms.string('mpa.root')
multiPhotonAnalyzer.doStoreCompCone = cms.untracked.bool(False)
multiPhotonAnalyzer.doStoreJets = cms.untracked.bool(False)

multiPhotonAnalyzer.gsfElectronCollection = cms.untracked.InputTag("ecalDrivenGsfElectrons")
multiPhotonAnalyzer.GammaEtaMax = cms.untracked.double(100)
multiPhotonAnalyzer.GammaPtMin = cms.untracked.double(10)

from RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff import *

from HeavyIonsAnalysis.JetAnalysis.ExtraEGammaReco_cff import *
from edwenger.HiTrkEffAnalyzer.TrackSelections_cff import *
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *

hiGoodTracks.src = cms.InputTag("hiGeneralTracks")
photonMatch.matched = cms.InputTag("hiGenParticles")
patPhotons.addPhotonID = cms.bool(False)
#interestingTrackEcalDetIds.TrackCollection = cms.InputTag("hiGeneralTracks")


photonStep = cms.Sequence(hiGoodTracks * 
                          photon_extra_reco * 
                          makeHeavyIonPhotons * 
                          selectedPatPhotons * 
                          multiPhotonAnalyzer)
photonStep.remove(interestingTrackEcalDetIds)
photonStep.remove(seldigis)

reducedEcalRecHitsEB.interestingDetIdCollections = cms.VInputTag(cms.InputTag("interestingEcalDetIdEB"), cms.InputTag("interestingEcalDetIdEBU"))
reducedEcalRecHitsEB.recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB")
reducedEcalRecHitsEB.reducedHitsCollection = cms.string('')

reducedEcalRecHitsEE.interestingDetIdCollections = cms.VInputTag(cms.InputTag("interestingEcalDetIdEE"))
reducedEcalRecHitsEE.recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE")
reducedEcalRecHitsEE.reducedHitsCollection = cms.string('')
