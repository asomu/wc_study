#
NE = [("Maine", 30840, 1.329), ("Vermont", 9217, .626), ("New Hampshire", 8953, 1.321), ("Massachusetts", 7800, 6.646), ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
NE.sort(key=lambda x:x[1], reverse=True)
for x,y,z in NE:
    print(x,y,z)

