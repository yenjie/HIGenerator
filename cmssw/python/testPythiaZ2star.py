import FWCore.ParameterSet.Config as cms

process = cms.Process("ANA")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("GeneratorInterface.HydjetInterface.hydjetDefault_cfi")
process.load('Configuration.StandardSequences.Generator_cff')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(500000)
                                       )

process.source = cms.Source("EmptySource")

process.load("Configuration.Generator.PythiaUEZ2starSettings_cfi");
process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(2760.0),
    PythiaParameters = cms.PSet(
        process.pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1               ! QCD hight pT processes', 
            'CKIN(3)=80.          ! minimum pt hat for hard interactions', 
            'CKIN(4)=9990.         ! maximum pt hat for hard interactions'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


process.RandomNumberGeneratorService.generator.initialSeed = 5

process.SimpleMemoryCheck = cms.Service('SimpleMemoryCheck',
                                        ignoreTotal=cms.untracked.int32(0),
                                        oncePerEventMode = cms.untracked.bool(False)
                                        )

process.ana = cms.EDAnalyzer('HydjetAnalyzer'
                             )


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('PythiaZ2Star.root')
                                   )


process.dijet1 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak1HiGenJets")
                              )
process.dijet2 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak2HiGenJets")
                              )
process.dijet3 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak3HiGenJets")
                              )
process.dijet4 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak4HiGenJets")
                              )
process.dijet5 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak5HiGenJets")
                              )
process.dijet6 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak6HiGenJets")
                              )
process.dijet7 = cms.EDAnalyzer("DijetNtupleProducer",
                               src3=cms.untracked.InputTag("ak7HiGenJets")
                              )




process.p1 = cms.Path(process.generator*
                      process.hiGenParticles*
		      process.hiGenJets*
		      process.dijet1*
		      process.dijet2*
		      process.dijet3*
		      process.dijet4*
		      process.dijet5*
		      process.dijet6*
		      process.dijet7*
		      process.ana)




