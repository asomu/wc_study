'''
f1 = open('test.txt', 'w')
f1.write('hello python')
f1.close()


f2 = open('test.txt','r')
rstr = f2.read()
print(rstr)
f2.close()



f3 = open('test2.txt','r')
for rd in f3:
    print(rd, end='')

f3.close()
'''

f4 = open('test2.txt','r')
rdata = [line.rstrip() for line in f4]
print(rdata)
