
import FWCore.ParameterSet.Config as cms

# Turn of MC dependence in pat sequence
def removePatMCMatch(process):
    process.prod.remove(process.genPartons)
    process.prod.remove(process.heavyIonCleanedGenJets)
    process.prod.remove(process.hiPartons)
    process.prod.remove(process.patJetGenJetMatch)
    process.prod.remove(process.patJetPartonMatch)
    
    process.patJets.addGenPartonMatch   = False
    process.patJets.embedGenPartonMatch = False
    process.patJets.genPartonMatch      = ''
    process.patJets.addGenJetMatch      = False
    process.patJets.genJetMatch      = ''
    process.patJets.getJetMCFlavour     = False
    process.patJets.JetPartonMapSource  = ''
    return process

# Top Config to turn off all mc dependence
def disableMC(process):
    process.prod.remove(process.heavyIon)
    removePatMCMatch(process)
    return process

def hltFromREDIGI(process):
    process.hltanalysis.HLTProcessName      = "REDIGI"
    process.hltanalysis.l1GtObjectMapRecord = cms.InputTag("hltL1GtObjectMap::REDIGI")
    process.hltanalysis.l1GtReadoutRecord   = cms.InputTag("hltGtDigis::REDIGI")
    process.hltanalysis.hltresults          = cms.InputTag("TriggerResults::REDIGI")   
    return process

def overrideBeamSpot(process):
    process.GlobalTag.toGet = cms.VPSet(
        cms.PSet(record = cms.string("BeamSpotObjectsRcd"),
                 tag = cms.string("Realistic2.76ATeVCollisions_STARTUP_v0_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_BEAMSPOT")
                 ),
        )
    return process


def addRPFlat(process):
    process.GlobalTag.toGet.extend([
        cms.PSet(record = cms.string("HeavyIonRPRcd"),
                 tag = cms.string("RPFlatParams_Test_v0_offline"),
                 connect = cms.untracked.string("frontier://FrontierPrep/CMS_COND_TEMP"),
                 ),
        ])
    return process


def overrideCentrality(process):
    process.GlobalTag.toGet.extend([

        #==================== MC Tables ====================
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFhits40_AMPTOrgan_v0_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("HFhitsAMPT_Organ")
                 ),
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_PixelHits40_AMPTOrgan_v0_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("PixelHitsAMPT_Organ")
                 ),
        
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFhits40_HydjetBass_vv44x04_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("HFhitsHydjet_Bass")
                                    ),
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_PixelHits40_HydjetBass_vv44x04_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("PixelHitsHydjet_Bass")
                 ),               
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_Tracks40_HydjetBass_vv44x04_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("TracksHydjet_Bass")
                 ),
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_PixelTracks40_HydjetBass_vv44x04_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("PixelTracksHydjet_Bass")
                 ),

        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFtowers40_HydjetBass_vv44x04_mc"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("HFtowersHydjet_Bass")   
                 ),        

    cms.PSet(record = cms.string("HeavyIonRcd"),
                              tag = cms.string("CentralityTable_HFhits40_HydjetDrum_vv44x05_mc"),
                              connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                              label = cms.untracked.string("HFhitsHydjet_Drum")
                                                 ),
                cms.PSet(record = cms.string("HeavyIonRcd"),
                                          tag = cms.string("CentralityTable_PixelHits40_HydjetDrum_vv44x05_mc"),
                                          connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                          label = cms.untracked.string("PixelHitsHydjet_Drum")
                                          ),
                cms.PSet(record = cms.string("HeavyIonRcd"),
                                          tag = cms.string("CentralityTable_Tracks40_HydjetDrum_vv44x05_mc"),
                                          connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                          label = cms.untracked.string("TracksHydjet_Drum")
                                          ),
                cms.PSet(record = cms.string("HeavyIonRcd"),
                                          tag = cms.string("CentralityTable_PixelTracks40_HydjetDrum_vv44x05_mc"),
                                          connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                          label = cms.untracked.string("PixelTracksHydjet_Drum")
                                          ),

                cms.PSet(record = cms.string("HeavyIonRcd"),
                                          tag = cms.string("CentralityTable_HFtowers200_HydjetDrum_v5315x01_mc"),
                                          connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                          label = cms.untracked.string("HFtowersHydjet_Drum")
                                          ),
        
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_PixelHits40_Glauber2010A_v3_effB_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("PixelHits")
                 ),
        
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFhits40_Glauber2010A_v3_effB_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("HFhits")
                 ),
        
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFtowers200_Glauber2010A_v5315x01_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("HFtowers")
                 ),

#==================== pPb data taking 2013 =====================================

         cms.PSet(record = cms.string("HeavyIonRcd"),
                   tag = cms.string("CentralityTable_HFplus100_PA2012B_v533x01_offline"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("HFtowersPlusTrunc")
                   ),
         cms.PSet(record = cms.string("HeavyIonRcd"),
                   tag = cms.string("CentralityTable_HFtrunc100_PA2012B_v538x02_offline"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("HFtowersTrunc")
                   ),

#==================== pPb MC 2013 =====================================

         cms.PSet(record = cms.string("HeavyIonRcd"),
                    tag = cms.string("CentralityTable_Tracks100_HijingPA_v538x02_mc"),
                    connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                    label = cms.untracked.string("TracksHijing")
                    ),
         cms.PSet(record = cms.string("HeavyIonRcd"),
                    tag = cms.string("CentralityTable_HFplus100_HijingPA_v538x02_mc"),
                    connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                    label = cms.untracked.string("HFtowersPlusTruncHijing")
                    ),
         cms.PSet(record = cms.string("HeavyIonRcd"),
                    tag = cms.string("CentralityTable_HFtrunc100_HijingPA_v538x01_mc"),
                    connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                    label = cms.untracked.string("HFtowersTruncHijing")
                    ),
         cms.PSet(record = cms.string("HeavyIonRcd"),
                    tag = cms.string("CentralityTable_HFplus100_EposPA_v538x01_mc"),
                    connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                    label = cms.untracked.string("HFtowersPlusTruncEpos")
                    ),
         cms.PSet(record = cms.string("HeavyIonRcd"),
                    tag = cms.string("CentralityTable_HFtrunc100_EposPA_v538x01_mc"),
                    connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                    label = cms.untracked.string("HFtowersTruncEpos")
                    ),

        ])
    return process

def overrideJEC_PbPb2760(process):
    process.GlobalTag.toGet.extend([

        #==================== JET CORRECTIONS

            cms.PSet(record = cms.string("JetCorrectionsRecord"),
                     tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKPu3PF_offline"),
                     connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                     label = cms.untracked.string("AKPu3PF_hiIterativeTracks")
                     ),
            cms.PSet(record = cms.string("JetCorrectionsRecord"),
                     tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKPu4PF_offline"),
                     connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                     label = cms.untracked.string("AKPu4PF_hiIterativeTracks")
                     ),
            cms.PSet(record = cms.string("JetCorrectionsRecord"),
                     tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKPu5PF_offline"),
                     connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                     label = cms.untracked.string("AKPu5PF_hiIterativeTracks")
                     ),
            
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKVs3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs3PF_hiIterativeTracks")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKVs4PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs4PF_hiIterativeTracks")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKVs5PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs5PF_hiIterativeTracks")
                 ),        
        
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_IC5Calo_2760GeV_v0_offline"),
                 # pp 7TeV version:       JetCorrectorParametersCollection_Fall12_V5_DATA_IC5Calo                                                                           
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("IC5Calo_2760GeV")
                 ),
        ])
    return process


def overrideJEC_pPb5020(process):
    process.GlobalTag.toGet.extend([

      cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v03_AK1Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK1Calo_HI")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK2Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK2Calo_HI")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK3Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK3Calo_HI")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK4Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK4Calo_HI")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK5Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK5Calo_HI")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK6Calo_offline"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK6Calo_HI")
                   ),

      cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK1PF_generalTracks")
                 ),

        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK2PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK3PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK4PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK4PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK5PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK5PF_generalTracks")
                 ),

###PLACEHOLDERS BEGIN###

      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKVs3PF_generalTracks")
               ),
      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK4PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKVs4PF_generalTracks")
               ),
      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK5PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKVs5PF_generalTracks")
               ),
      
      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKPu3PF_generalTracks")
               ),
      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK4PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKPu4PF_generalTracks")
               ),
      cms.PSet(record = cms.string("JetCorrectionsRecord"),
               tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK5PF_offline"),
               connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
               label = cms.untracked.string("AKPu5PF_generalTracks")
               ),
      
###PLACEHOLDERS END###
      

         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK6PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK7PF_generalTracks")
                 ),

        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v03_AK1Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu1Calo_HI")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK2Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu2Calo_HI")
                 ),

         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu3Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu3Calo_HI")
                 ),

         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu4Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu4Calo_HI")
                 ),

        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu5Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu5Calo_HI")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK6Calo_offline"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu6Calo_HI")
                   ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu1PF_generalTracks")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu2PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu3PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu4PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu4PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu5PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu5PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu6PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu7PF_generalTracks")
                 ),


### more placeholders for Vs
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v03_AK1Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs1Calo_HI")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK2Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs2Calo_HI")
                 ),

         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu3Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs3Calo_HI")
                 ),

         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu4Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs4Calo_HI")
                 ),

        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v08_AKPu5Calo_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs5Calo_HI")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK6Calo_offline"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKVs6Calo_HI")
                   ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs1PF_generalTracks")
                 ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs2PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs3PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu4PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs4PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v08_AKPu5PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs5PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs6PF_generalTracks")
                 ),
         cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs7PF_generalTracks")
                 ),


        

        ])

    return process


def overrideJEC_Pbp5020MC(process):

      process.GlobalTag.toGet.extend([


          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AK3Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK3Calo_HI")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AK4Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK4Calo_HI")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AK5Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK5Calo_HI")
                   ),
          
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AKPu3Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu3Calo_HI")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AKPu4Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu4Calo_HI")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v15_reversed_AKPu5Calo_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu5Calo_HI")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AK3PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK3PF_generalTracks")
                   ),

          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AK4PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK4PF_generalTracks")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AK5PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AK5PF_generalTracks")
                   ),
                    
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AKPu3PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu3PF_generalTracks")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AKPu4PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu4PF_generalTracks")
                   ),
          
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v15_reversed_AKPu5PF_mc"),
                   connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                   label = cms.untracked.string("AKPu5PF_generalTracks")
                   ),
          
                 ])

      return process




def overrideJEC_pp2760(process):
    process.GlobalTag.toGet.extend([

                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_pp_PythiaZ2_2760GeV_538_v85_AK3Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK3Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AK4Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK4Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AK5Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK5Calo_HI")
                                             ),                                    


                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_pp_PythiaZ2_2760GeV_538_v85_AK3Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu3Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKPu4Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu4Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKPu5Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu5Calo_HI")
                                             ),
                                    
                                    
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_pp_PythiaZ2_2760GeV_538_v85_AK3Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs3Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKVs4Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs4Calo_HI")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PythiaZ2_2760GeV_5316_v14_AKVs5Calo_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs5Calo_HI")
                                             ),
                                    
                                    

                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK1PF_generalTracks")
                                             ),                                    
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK2PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK3PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK3PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK4PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK4PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK5PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK5PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK6PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AK7PF_generalTracks")
                                             ),
              
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu1PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu2PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK3PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu3PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK4PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu4PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_2760GeV_538_v09_AK5PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu5PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu6PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKPu7PF_generalTracks")
                                             ),

###PLACEHOLDERS BEGIN###
                                    
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs3PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK4PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs4PF_generalTracks")
                                             ),
                                    cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                             tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK5PF_offline"),
                                             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                                             label = cms.untracked.string("AKVs5PF_generalTracks")
                                             ),

        
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs2PF_generalTracks")
             ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKPu2Calo_HI")
             ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AKVs2Calo_HI")
             ),
        cms.PSet(record = cms.string("JetCorrectionsRecord"),
                 tag = cms.string("JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline"),
                 connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
                 label = cms.untracked.string("AK2Calo_HI")
             ),
        
                                    
                                    ###PLACEHOLDERS END###


        
        ])
    
    return process

#======  Final default common functions including centrality

def overrideGT_pPb5020(process):
    overrideCentrality(process)
    overrideJEC_pPb5020(process)
    return process

def overrideGT_pp2760(process):
    overrideCentrality(process)
    overrideJEC_pp2760(process)
    return process

def overrideGT_PbPb2760(process):
    overrideCentrality(process)
    overrideJEC_PbPb2760(process)
    return process

            
