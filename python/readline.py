import sys
f1 = open(sys.argv[1],'r',encoding='utf-8')
f2 = open('freq.dat', 'w+',encoding='utf-8')

search = ['Mode','Frequency',"IR Intens"]
mode=[]
freq=[]
intens=[]
#for line in iter(f1):
#  if line.startswith('Mode:'):
#line = f1.readline()
for line in f1:
    if '\n' == line[-1]:
        line = line[:-1]
    line = line.strip()
# get rid of the space before each line
    if line.startswith("Mode"):
        list = line.strip().split()
        for item in list[1:]:
            mode.append(item)
            
    if line.startswith(search[1]):
        list = line.split()
        for item in list[1:]:
            freq.append(item)
            
    if line.startswith(search[2]):
        list = line.strip().split()
        for item in list[2:]:
            intens.append(item) 
                       
for i in range(1,len(mode)):
    print(mode[i-1]+' '+freq[i-1]+ ' ' + intens[i-1])
#    print(freq)
#    print(intens)
#print(len(mode))

#    fi.write(str(line))
f1.close
f2.close
