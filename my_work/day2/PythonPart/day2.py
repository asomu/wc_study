sentence = 'it is good day'

words = sentence.split()
data4 = [[w.lower(), w.upper(), len(w)] for w in words if len(w) > 2]

print(data4)

for idx, word in enumerate(words):
    print(f"{idx}: {word}")


alist = ['a1','a2','a3','a4']
blist = ['b1','b2','b3']

c = zip(alist, blist)
d = list(c)
print(c)
print(d)
for a, b in zip(alist, blist):
    print(a,b)

data = [1,2,3,4]

result = list(map(lambda x:x**x, data))
print(result)
