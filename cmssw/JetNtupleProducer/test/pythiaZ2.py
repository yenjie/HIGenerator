import FWCore.ParameterSet.VarParsing as VarParsing

ivars = VarParsing.VarParsing('python')

ivars.register ('randomNumber',
                                1,
                                ivars.multiplicity.singleton,
                                ivars.varType.int,
                                "Random Seed")

ivars.randomNumber = 1
ivars.inputFiles = "file:preMix_440_C_numEvent1.root"
ivars.outputFile = '/afs/cern.ch/user/d/dgulhan/workDir/mixed_440_B_01.root'

ivars.parseArguments()


import FWCore.ParameterSet.Config as cms

process = cms.Process("ANA")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.RandomNumberGeneratorService.generator.initialSeed = ivars.randomNumber
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealisticPPbBoost8TeVCollision_cff')
process.load('PhysicsTools.HepMCCandAlgos.HiGenParticles_cfi')
process.load('RecoHI.HiJetAlgos.HiGenJets_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraGenReco_cff')
process.load('PhysicsTools.JetMCAlgos.SelectPartons_cff')

process.hiGenParticles.srcVector = ["generator"]

process.load("Configuration.Generator.PythiaUEZ2Settings_cfi");
process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(5020.0),
    # comEnergy = cms.double(2760.0),
    PythiaParameters = cms.PSet(
        process.pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1               ! QCD hight pT processes', 
            'CKIN(3)=30.          ! minimum pt hat for hard interactions', 
            'CKIN(4)=9990.         ! maximum pt hat for hard interactions'),
            # 'VINT(10)=5'),
            
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings','processParameters')
        # parameterSets = cms.vstring('processParameters')
    )
)


# process.Realistic5TeVCollisionPPbBoostVtxSmearingParameters.Beta=0.434

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(50)
                                       )

process.SimpleMemoryCheck = cms.Service('SimpleMemoryCheck',
                                        ignoreTotal=cms.untracked.int32(0),
                                        oncePerEventMode = cms.untracked.bool(False)
                                        )

process.gen = cms.EDAnalyzer('HydjetAnalyzer')
process.dijet = cms.EDAnalyzer('DijetNtupleProducer')

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string(ivars.outputFile)
                                   )

process.myPartons.src = cms.InputTag("hiGenParticles")

process.p = cms.Path(
    process.generator*
    process.VtxSmeared*
    process.hiGen *
	process.myPartons *
    process.ak3HiGenJets *
    process.ak5HiGenJets *
    process.gen*
    process.dijet
    )








