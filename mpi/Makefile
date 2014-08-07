objects = fileio.o
FC = mpif90
#FC = ftn
switch = -O3 #-w
EXEC = fileio 
#FLAGS = -heap-arrays
#EXEC2 = cont
#LIB = /usr/lib64/atlas/liblapack.so.3.0
#LIB = -llapack  
#LIB = -mkl=parallel

$(EXEC): $(objects)
	$(FC) -o $(EXEC) $(FLAGS) $(LIB) $(switch) $(objects)

%.mod: %.f90
	$(FC) -c $<

%.o: %.f
	$(FC) -c $<

%.o: %.f90
	$(FC) -c $<

clean:
	rm $(objects) $(EXEC)
veryclean:
	rm *.o *.dat *.mod
