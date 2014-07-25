#include <iostream>
#include <cmath>

#include "boost/lexical_cast.hpp"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "GeneratorInterface/Core/interface/RNDMEngineAccess.h"

#include "GeneratorInterface/JewelInterface/interface/JewelHadronizer.h"
#include "GeneratorInterface/JewelInterface/interface/JewelPythiaWrapper.h"
#include "GeneratorInterface/JewelInterface/interface/JewelWrapper.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "HepMC/IO_HEPEVT.h"
#include "HepMC/GenEvent.h"
#include "HepMC/HeavyIon.h"
#include "HepMC/SimpleVector.h"
#include "CLHEP/Random/RandomEngine.h"

static const double pi = 3.14159265358979;

using namespace edm;
using namespace std;
using namespace gen;

HepMC::IO_HEPEVT hepevtio;

JewelHadronizer::JewelHadronizer(const ParameterSet &pset) :
    BaseHadronizer(pset),
    evt(0), 
    pset_(pset),
    bmax_(pset.getParameter<double>("bMax")),
    bmin_(pset.getParameter<double>("bMin")),
    efrm_(pset.getParameter<double>("comEnergy")),
    frame_(pset.getParameter<string>("frame")),
    proj_(pset.getParameter<string>("proj")),
    targ_(pset.getParameter<string>("targ")),
    iap_(pset.getParameter<int>("iap")),
    izp_(pset.getParameter<int>("izp")),
    iat_(pset.getParameter<int>("iat")),
    izt_(pset.getParameter<int>("izt")),
    phi0_(0.),
    sinphi0_(0.),
    cosphi0_(1.),
    rotate_(pset.getParameter<bool>("rotateEventPlane"))
{
  // Default constructor
  Service<RandomNumberGenerator> rng;
  hijRandomEngine = &(rng->getEngine());

}


//_____________________________________________________________________
JewelHadronizer::~JewelHadronizer()
{
  // destructor
}

//_____________________________________________________________________
void JewelHadronizer::add_heavy_ion_rec(HepMC::GenEvent *evt)
{
  // heavy ion record in the final CMSSW Event
  HepMC::HeavyIon* hi = new HepMC::HeavyIon(
    0,                               // Ncoll_hard/N of SubEvents
    0,                               // Npart_proj
    0,                               // Npart_targ
    0, // Ncoll
    0,                                   // spectator_neutrons
    0,                                   // spectator_protons
    0,                          // N_Nwounded_collisions
    0,                          // Nwounded_N_collisions
    0,                          // Nwounded_Nwounded_collisions
    //gsfs Changed from 19 to 18 (Fortran counts from 1 , not 0) 
    0,                   // impact_parameter in [fm]
    0,                               // event_plane_angle
    0,                                   // eccentricity
    //gsfs Changed from 12 to 11 (Fortran counts from 1 , not 0) 
    0                    // sigma_inel_NN
  );
  evt->set_heavy_ion(*hi);
  delete hi;
}

//___________________________________________________________________     
HepMC::GenParticle* JewelHadronizer::build_hijing(int index, int barcode)
{
   // Build particle object corresponding to index in hijing

/*                                                                                                                                                         
   double x0 = himain2.patt[0][index];
   double y0 = himain2.patt[1][index];

   double x = x0*cosphi0_-y0*sinphi0_;
   double y = y0*cosphi0_+x0*sinphi0_;

   // Jewel gives V0's status=4, they need to have status=1 to be decayed in geant
   // also change status=11 to status=2
   if(himain2.katt[3][index]<=10 && himain2.katt[3][index]>0) himain2.katt[3][index]=1;
   if(himain2.katt[3][index]<=20 && himain2.katt[3][index]>10) himain2.katt[3][index]=2;

   HepMC::GenParticle* p = new HepMC::GenParticle(
                                                  HepMC::FourVector(x,  // px                                                                            
                                                                    y,  // py                                                                            
                                                                    himain2.patt[2][index],  // pz                                                         
                                                                    himain2.patt[3][index]), // E                                                          
                                                  himain2.katt[0][index],// id                                                                             
                                                  himain2.katt[3][index] // status                                                          
                                                  );
   p->suggest_barcode(barcode);
   
   return p;
*/
   return 0;
}

//___________________________________________________________________     
HepMC::GenVertex* JewelHadronizer::build_hijing_vertex(int i,int id)
{
   return 0;
}

bool JewelHadronizer::generatePartonsAndHadronize()
{
   // generate a JEWEL event
   static int j=0;
   j++;
   GENEVENT(j);
   call_pyhepc(1);
   
   HepMC::GenEvent* evt = hepevtio.read_next_event();

   evt->set_signal_process_id(pypars.msti[0]);	 // type of the process
   evt->set_event_scale(pypars.pari[16]);  	 // Q^2

   //if(embedding_) rotateEvtPlane(evt,evtPlane_);
   //add_heavy_ion_rec(evt);
   event().reset(evt);
   return true;
}

//_____________________________________________________________________  
bool JewelHadronizer::get_particles(HepMC::GenEvent *evt )
{      
}

//_____________________________________________________________________
bool JewelHadronizer::call_hijset(double efrm, std::string frame, std::string proj, std::string targ, int iap, int izp, int iat, int izt)
{
   INIT();
      
   return true;
}

//______________________________________________________________
bool JewelHadronizer::initializeForInternalPartons(){

  //initialize pythia5

//  if(0){
//    std::string dumstr = "";
//    call_pygive(dumstr);
//  }

   // initialize hijing
//   LogInfo("HIJINGinAction") << "##### Calling HIJSET(" << efrm_ << "," <<frame_<<","<<proj_<<","<<targ_<<","<<iap_<<","<<izp_<<","<<iat_<<","<<izt_<<") ####";
//   call_hijset(efrm_,frame_,proj_,targ_,iap_,izp_,iat_,izt_);

   return true;

}

bool JewelHadronizer::declareStableParticles( std::vector<int> pdg )
{
   return true;
}

//________________________________________________________________                                                                    
void JewelHadronizer::rotateEvtPlane(){

   phi0_ = 2.*pi*gen::hijran_(0) - pi;
   sinphi0_ = sin(phi0_);
   cosphi0_ = cos(phi0_);
}

//________________________________________________________________ 
bool JewelHadronizer::hadronize()
{
   return false;
}

bool JewelHadronizer::decay()
{
   return true;
}
   
bool JewelHadronizer::residualDecay()
{  
   return true;
}

void JewelHadronizer::finalizeEvent(){
    return;
}

void JewelHadronizer::statistics(){
    return;
}

const char* JewelHadronizer::classname() const
{  
   return "gen::JewelHadronizer";
}

