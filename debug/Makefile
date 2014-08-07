CXX = g++
CXXFLAGS = -g -Wall 

qm: fact.cc
	$(CXX) $(CXXFLAGS) $^ -o $@
%.o: %.cc
	$(CXX) -c $^
clean:
	/bin/rm -f *.o 

