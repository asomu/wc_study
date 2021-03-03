'''
* 0번이상
+ 1번이상
[A-Z] 안에 있는 문자 중 하나
() 그룹화할 때
{m, n} m번 이상 n번 이하 문자들이 나타남
[^] 해당문자 제외한.
| 표현식중 하나
. 문자하나
^ 맨앞
$ 맨마지막
\ 특수문자
?! 포함하지 않는다.
'''
import re

r1 = re.compile('hello')

fobj = re.search(r1, 'good hello world')
print(fobj)
print(fobj.span())
print(fobj.group())

fobj2 = re.search(r"hello", 'good hello world')
print(fobj2)
print(fobj2.span())
print(fobj2.group())

fdata1 = re.findall(r"hello", 'good hello world good hello world')
print(fdata1)

fdata2 = re.findall(r"a+b*", 'aaaa cc abbbb aabb a')
print(fdata2)

fdata3 = re.findall(r"[a-zA-Z0-9]+@A-Z.(com|net)", 'aaaa cc abbbb asomu@naver.com')
print(fdata3)

fdata4 = re.findall(r"[0-9A-Z]+\.+[a-zA-Z]", 'aaaa cc abbbb aabb 123A worl12234')
print(fdata4)

fdata5 = re.findall(r"h{2,3}", 'h  hhhh aaaa cc abbbb aabb 123A worl12234')
print(fdata5)

fdata6 = re.findall(r"\d{3}-\d{3,4}-\d{4}", '010-8107-0063-12314 11-154-4849 121-123-124-1555')
print(fdata6)

fdata7 = re.findall(r"\w+", '010-8107-0063-12314 11-154-4849 121-123-124-1555')
print(fdata7)
#\w 특수기호 제외.
#\W 특수기호 만.
#\d 숫자만
#\D 숫자제외