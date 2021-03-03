infile1 = open('File1.txt', 'r')
infile2 = open('File2.txt', 'r')

sdata1 = {line for line in infile1}
sdata2 = {line for line in infile2}

infile1.close()
infile2.close()

outfile1 = open('Union.txt', 'w')
outfile1.writelines(sdata1 | sdata2)

outfile2 = open('Intersection.txt', 'w')
outfile2.writelines(sdata1 & sdata2)

outfile3 = open('Difference.txt', 'w')
outfile3.writelines(sdata1 - sdata2)

outfile3.close()

outfile1.close()
outfile2.close()
