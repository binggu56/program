import sys

#fn = input("Enter the name of the geometry file:")
fi = open(sys.argv[1],'r')
fi2= open('geo.xyz','w')
for i,line in enumerate(fi):
    if line.startswith('H'):
        fi2.write(str(i+1) + "  2.01401\n")
        

           
