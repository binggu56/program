objects = test.o
FC = gfortran
switch = -O3
EXEC = qm
#LIB = /usr/lib64/atlas/liblapack.so.3.0
#LIB = -llapack 
FFLAGS = -fopenmp
$(EXEC): $(objects)
	$(FC) $(FFLAGS) -o $(EXEC) $(LIB) $(switch) $(objects)
%.o: %.f90
	$(FC) $(FFLAGS)  -c  $<
#%.O: %.f
#	$(FC) -c $<

clean:
	rm $(objects)
veryclean:
	rm *.o
