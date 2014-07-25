C*********************************************************************
 
      program yajem_run
C... Start of the event loop

      call init()
C...Generate nevent events of each required type.
      DO 220 IEVT=1,nevent
         call generateEvent()
 220  CONTINUE



 2000    FORMAT('OSC1997A'/'final_id_p_x')
 2100    FORMAT(' YaJEM  ',5X,F5.3,2X,'(',I3,',',I6,')+(',I3,',',I6,')',
     &        2X,A4,2X,D10.4,2X,I8)
 2200    FORMAT('!'/'! Listing of ',I6,' collision events:'/'!')
 2300    FORMAT(I10,2X,I10,2X,F8.3,2X,F8.3)
 2400 FORMAT(I10,2X,I10,2X,D12.6,2X,D12.6,2X,D12.6,2X,D12.6,2X,
     &D12.6,2X,D12.6,2X,D12.6,2X,D12.6,2X,D12.6)
csab, oscar modifications
c 2400    FORMAT(I10,2X,I10,2X,D12.6,2X,D12.6,2X,D12.6,2X,D12.6,2X,
c     &        D12.6,2X,D12.6,2X,D12.6,2X,D12.6,2X,D12.6,2X,D12.6)

 3000	FORMAT(D12.6,2X,D12.6) 
 3001	FORMAT(I10)
 3002	FORMAT(D12.6,2X,D12.6,2X,D12.6) 
      RETURN
      END
 
      integer function init() 
C...Double precision and integer declarations.
      IMPLICIT DOUBLE PRECISION(A-H, O-Z)
      IMPLICIT INTEGER(I-N)
      INTEGER PYK,PYCHGE,PYCOMP

      character*4 reffram 

C...Commonblocks.
      COMMON/PYJETS/N,NPAD,K(4000,5),P(4000,5),V(4000,5)
      COMMON/PYDAT1/MSTU(200),PARU(200),MSTJ(200),PARJ(200)
      COMMON/PYDAT2/KCHG(500,4),PMAS(500,4),PARF(2000),VCKM(4,4)
      COMMON/PYDAT3/MDCY(500,3),MDME(4000,2),BRAT(4000),KFDP(4000,5)
      COMMON/PYSUBS/MSEL,MSELPD,MSUB(500),KFIN(2,-40:40),CKIN(200)
      COMMON/PYPARS/MSTP(200),PARP(200),MSTI(200),PARI(200)
      COMMON/PYINT1/MINT(400),VINT(400)
      COMMON/PYDATR/MRPY(6),RRPY(100)
      COMMON/YADAT/YAPROFILET(500),YAPROFILEQ(500),YAPROFILEINT(500)
      COMMON/YADAT1/YAPARS(20),YAFLAGS(20)
      SAVE /PYJETS/,/PYDAT1/,/PYDAT2/,/PYDAT3/,/PYSUBS/,/PYPARS/,
     &     /PYINT1/,/YADAT/,/YADAT1/
C...Local arrays.
      DIMENSION PSUM(5),PINI(6),PFIN(6)

c conversion from mm to fm/c
      mm_to_fmc=1d3/(1d-15/2.99792458d8)

      
C...Standard PYTHIA flags influencing how the shower is done - can usually be left at their defaults
C...but some are worth setting if photon production or a different fragmentation model is needed


c       MSTJ(1)=2 ! 1: Lund 2: independent fragmentation
c       MSTJ(2)=1 ! 1: fragments like q 3: fragments like qqbar pair      
c       MSTJ(3)=2 ! conservation laws to be imposed
c       MSTJ(21)=0 ! 0: no particle decays 2: default
c	MSTJ(22)=2 ! decay particles only when average lifetime is shorter than PARJ(71)
c	PARJ(71)=0.1 ! decay length in mm
       MSTJ(41)=1 ! 1: QCD branchings 2: QCD + QED branchings 10: QED branchings enhanced by PARJ(84)
c       MSTJ(42)=1 ! 1: no angular coherence, 2: coherence 3: coherence with mass effect
c       MSTJ(44)=0 ! 0: fixed 2: run alpha_s in shower     	
c	PARU(111)=0.3 ! fixed alpha s
	PARJ(84)=10.0 ! enhancement for e.m. emissions
c	PARJ(81)=0.2 ! Lambda


C... MSTJ(43) needs to be 3 for YaJEM to properly work, do not change!
       MSTJ(43)=3 ! z definition 1: lc 2: lu 3: gc 4: gu 

C... PARJ(82) is the crucial parameter for YaJEM-D functionality - the min Q^2 scale must be set to 
C... sqrt(E/L) once parton energy E and medium length L are known

	PARJ(82)=1.0D0 ! min Q for branching


c	YaJEM-specific parameters and flags
	YAPARS(1)=0.0D0 ! f_med parameter enhancing branching kernels
	YAPARS(2)=3.0D0 ! Delta Q^2 integrated along parton path, i.e. normalization of profile.dat 
	YAPARS(3)=0.8D0 ! coefficient linking YAPARS(2) and induced radiation
	YAPARS(4)=0.1D0 ! coefficient linking YAPARS(2) and drag force

	YAPARS(10)=0.5D0 ! for use with YAFLAGS(3)=1, max. medium temperature corresponding to initial value in profile.dat

	YAFLAGS(1)=0 ! additional debug info on/off (0)
	YAFLAGS(2)=1 ! probabilistic parton formation time on/off (1)
	YAFLAGS(3)=0 ! jet-photon conversion model on/off (0) !Experimental!


c... define back-to-back parton pair

	ip=-1
	kf1=1
	kf2=-1  
	pecm=40.0D0

c... the random number generator seed
	MRPY(1)=11035493


c set number of events
      nevent=100000


C...The matter profile to be evaluated is loaded here. The file just needs to contain the shape of qhat(xi)
C...as probed by the parton, the normalization of the integral is enforced to be unity at this point and the 
C...normalization is set via YAPARS(2)
C...The arrays may also be set by other means if desired by the user 


	QNORM = 0.0D0
 	OPEN(50,FILE='profile.dat',STATUS='UNKNOWN')
     	DO  IPRO=1,500
	    READ(50,*) YAPROFILET(IPRO), YAPROFILEQ(IPRO)
	    QNORM = QNORM + YAPROFILEQ(IPRO)
	END DO
	CLOSE(50)
	
	QSUM = 0.0D0
	DO IPRO=1,500
		QSUM = QSUM + YAPROFILEQ(IPRO)/QNORM
		YAPROFILEINT(IPRO) = QSUM
	END DO
	
        end


        integer function generateEvent()
C...Commonblocks.
      COMMON/PYJETS/N,NPAD,K(4000,5),P(4000,5),V(4000,5)
      COMMON/PYDAT1/MSTU(200),PARU(200),MSTJ(200),PARJ(200)
      COMMON/PYDAT2/KCHG(500,4),PMAS(500,4),PARF(2000),VCKM(4,4)
      COMMON/PYDAT3/MDCY(500,3),MDME(4000,2),BRAT(4000),KFDP(4000,5)
      COMMON/PYSUBS/MSEL,MSELPD,MSUB(500),KFIN(2,-40:40),CKIN(200)
      COMMON/PYPARS/MSTP(200),PARP(200),MSTI(200),PARI(200)
      COMMON/PYINT1/MINT(400),VINT(400)
      COMMON/PYDATR/MRPY(6),RRPY(100)
      COMMON/YADAT/YAPROFILET(500),YAPROFILEQ(500),YAPROFILEINT(500)
      COMMON/YADAT1/YAPARS(20),YAFLAGS(20)
      SAVE /PYJETS/,/PYDAT1/,/PYDAT2/,/PYDAT3/,/PYSUBS/,/PYPARS/,
     &     /PYINT1/,/YADAT/,/YADAT1/
C...Local arrays.
        
c run in back-to-back jet pair mode

	ip=-1
	kf1=1
	kf2=-1  
	pecm=40.0D0

	call py2ent(ip,kf1,kf2,pecm)
	call pyshow(1,2, pecm/2.0D0)
	call pyexec

	call pyedit(1) !1: final state only 5: fragmenting partons + final state



C... The following blocks contain various routines to find the leading and subleading hadron, subject
C... to PID cuts. This can be used to write out only events which fulfill a hard track condition.


C...go through the event and find the highest p_T hadron
    
	nparticles=PYK(0,1) !gets the number of lines in the event record
	p_T_max=0.0D0
	E_trig=0.0D0

       DO iparticle = 1,nparticles

	p_T=P(iparticle,3)



	IF(p_T.eq.0.0D0) THEN 
		p_T = 1.0D0
	ENDIF




c... this is a condition for charged hadron production, only high P_T tracks are condidered
	IF((K(iparticle,2).EQ.211).OR.(K(iparticle,2).eq.-211).OR.(K(iparticle,2).eq.321).OR.(K(iparticle,2).eq.-321).OR.(K(iparticle,2).eq.2212).OR.(K(iparticle,2).eq.-2212)) THEN


	 IF(p_T.gt.p_T_max) THEN
	 	p_T_max=p_T
 	 ENDIF 
	
	ENDIF ! of the PID

 	END DO

C... go through the event and find the NL fragmentation hadron

	p_T_second=0D0

	DO iparticle = 1, nparticles

	p_T=P(iparticle,3)
	IF((K(iparticle,2).EQ.211).OR.(K(iparticle,2).eq.-211).OR.(K(iparticle,2).eq.321).OR.(K(iparticle,2).eq.-321).OR.(K(iparticle,2).eq.2212).OR.(K(iparticle,2).eq.-2212)) THEN
	IF((p_T.gt.p_T_second).AND.(p_T.lt.p_T_max)) THEN
		p_T_second=p_T


	ENDIF 
	ENDIF

	END DO




C...standardized output written to YaJEM_OSC.DAT, according to the
C...OSCAR (Open Standard Codes At RHIC) conventions, RIKEN-BNL, 1997.
         IF(IEVT.EQ.1) THEN
	    VERS=1.0D0
            IBM1=-1
            IBM2=mint(11)
            ITG1=-1
            ITG2=mint(12)
            
            OPEN(30,FILE='YaJEM_OSC.dat',STATUS='UNKNOWN')
            WRITE(30,2000)
            WRITE(30,2100) VERS,IBM1,IBM2,ITG1,ITG2,reffram,
     &           pesum,0
csab, oscar modifications

         ENDIF


	

C... write the event only if a high p_T hadron was observed, this allows to store only triggered events
C... with an evaluation of the trigger condition early on
	


	IF(p_T_max.gt.0.0D0) THEN
c		

         WRITE(30,2300) IEVT,N,bimp,0d0

         WRITE(30,2400) (I,K(I,2),(P(I,J),J=1,5),(V(I,J),
     &        J=1,4),I=1,N)


	ENDIF

         IF(IEVT.EQ.nevent) CLOSE(30)

 
         end
