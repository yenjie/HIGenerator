YaJEM
=====
http://www.phy.duke.edu/~trenk/yajem/

YaJEM is a Monte-Carlo (MC) generator for the in-medium evolution of QCD parton showers. It is based on the PYSHOW algorithm which is part of the PYTHIA package and modifies the kinematics of propagating states based on user-specified transport coefficients.
Download

YaJEM is based on the modified Fortran code of the PYSHOW algorithm of the PYTHIA 6 package. Download the YaJEM package from the link below, save in a subdirectory of your choice and unpack. The result should be a manual, two Fortran files yajem.f and pythia_yajem.f and a data file profile.dat. Please refer to the manual for further instructions.

Version and revision log

Version 1.1: added user control parameters to yajem.f and a user's manual

Version 1.0: basic version of YaJEM, was distributed on request

g77 -o yajem yajem.f pythia_yajem.f

or has been reported to compile using gfortran with

gfortran -fno-range-check -ffixed-line-length-180 -o yajem yajem.f pythia_yajem.f

Data format
===========

event npart bimp phi
where 
event	:	integer - event number
npart	:	integer - number of particles in an event
bimp	:	float - impact parameter
phi	:	float - azimuthal angle

No more comments are allowed after the event header.

There are npart number of lines each describes one particle in the format

ipart, id, px, py, pz, p0, mass, x, y, z, t
