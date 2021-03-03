import re

robj1 = re.match(r'[a-zA-Z0-9]+', '-Hello1234')
print(robj1)


robj3 = re.match(r'(?P<func>[a-zA-Z_][a-z_]+)\((?P<arg>\w+)\)', 'print(2323)')
print(robj3.groups())


b = re.sub(r'내가', lambda x:x.group() + '유어와이프', '내가 아침에 밥을 먹었다.')
print(b)

cstr5 = re.sub(r'([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1','hello 5232')
print(cstr5)

cstr6 = re.sub(r'({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>','{ "name": "kim" }')
print(cstr6)