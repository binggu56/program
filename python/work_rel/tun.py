import math
import sys
fo = open('tran.dat','w')
a = 1.0
en = 0.0001
while True:
    fo.write(str('{:f}'.format(en))+'\n')
    en+=0.01
    if(en >= 4.0):
        break



