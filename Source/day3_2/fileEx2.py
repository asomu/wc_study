infile = open('UNbyArea.txt','r')
ldata = [line.rstrip() for line in infile]
for i in range(len(ldata)):
    ldata[i] = ldata[i].split(',')
    ldata[i][1] = eval(ldata[i][1])

print(ldata)
