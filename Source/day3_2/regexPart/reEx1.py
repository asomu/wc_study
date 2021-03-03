import re

r1 = re.compile('Hello')
fobj1 = re.search(r1, 'good Hello World')
print(fobj1)
print(fobj1.span())
print(fobj1.group())

fobj2 = re.search(r'Hello', 'good Hello World')
print(fobj2)
print(fobj2.span())
print(fobj2.group())

fobj3 = re.search('Hello', 'good Hello World')
print(fobj3)
print(fobj3.span())
print(fobj3.group())

print()
fdata1 = re.findall(r'Hello', 'good Hello World Hello')
print(fdata1)

print()
fdata2 = re.findall(r'a+b*', 'aaaa cc bbb aabb')
print(fdata2)

print()
fdata3 = re.findall(r'^Hello', 'Hello good Hello World Hello')
print(fdata3)

print()
fdata4 = re.findall(r'[0-9]+', 'good 123Hello World579 Hello')
print(fdata4)


print()
fdata5 = re.findall(r'h{2}.', 'good 123Hello hhKim World579 Hello')
print(fdata5)

print()
fdata6 = re.findall(r'h{2,3}.', 'good 123Hello hhKim Worlhhhleed579 Hello')
print(fdata6)

print()
fdata7 = re.findall(r'\d{3}-[0-9]{3,4}-[0-9]{4}', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata7)

print()
fdata8 = re.findall(r'[a-zA-Z]+', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata8)

print()
fdata9 = re.findall(r'\d+', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata9)

print()
fdata10 = re.findall(r'\D+', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata10)

print()
fdata10 = re.findall(r'\w+', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata10)

print()
fdata11 = re.findall(r'\W+', 'good tel:010-787-8989 hhKim tel->010-8989-7979 Hello')
print(fdata11)




