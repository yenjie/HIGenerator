all: jewel-2.0.1-vac jewel-2.0.1-simple

# path to LHAPDF library
LHAPDF_PATH := /data/yjlee/HIGenerator/jewel/local/lib

FC := gfortran
FFLAGS := -g -static

jewel-2.0.1-vac: jewel-2.0.1.o medium-vac.o pythia6425mod.o meix.o
	$(FC) -o $@ -L$(LHAPDF_PATH) $^ -lLHAPDF

jewel-2.0.1-simple: jewel-2.0.1.o medium-simple.o pythia6425mod.o meix.o
	$(FC) -o $@ -L$(LHAPDF_PATH) $^ -lLHAPDF

clean:
	rm -f medium-*.o 
	rm -f jewel*.o
	rm -f pythia6425mod.o meix.o
	rm -f *~

.PHONY: all
