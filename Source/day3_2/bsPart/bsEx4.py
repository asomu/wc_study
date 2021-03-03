from bs4 import BeautifulSoup

html_str="""
<html>
    <body>
        <ul class='greet'>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class='replay'>
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bsObj = BeautifulSoup(html_str, 'html.parser')
ul_replay = bsObj.find('ul',{'class':'replay'})
print(ul_replay)

print()
lis = ul_replay.findAll('li')
for li in lis:
    print(li.text)
