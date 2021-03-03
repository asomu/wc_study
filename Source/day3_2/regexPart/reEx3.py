import re

cstr1 = re.sub(r'apple|orange', 'fruit', 'apple box orange box')
print(cstr1)

cstr2 = re.sub(r'내|나의|내꺼', '그의', '나의 물건에 손대지 마시오.')
print(cstr2)

def multi10(m):
    n = int(m.group())
    return str(n * 10)

cstr3 = re.sub(r'[0-9]+',multi10 ,'1 2 function 4 fruit 7 8');
print(cstr3)

cstr4 = re.sub(r'[0-9]+',lambda m : str(int(m.group())*5),'1 2 function 4 fruit 7 8');
print(cstr4)


cstr5 = re.sub(r'([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1','hello 5232')
print(cstr5)

cstr5 = re.sub(r'({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>','{ "name": "kim" }')
print(cstr5)
