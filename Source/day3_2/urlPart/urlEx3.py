from urllib.request import urlopen
import re
import urllib.request

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urlopen(url)
html_content = str(html.read().decode('utf8'))
#print(html_content)

url_list = re.findall(r'(http)(.+)(zip)', html_content)
#print(url_list)

for url in url_list:
    full_url = ''.join(url)
    file_name = re.findall(r'(ipg)(.+)(zip)', full_url)
    #print(file_name)
    if len(file_name) > 0:
        file_name = ''.join(file_name[0])
        #print(file_name)
        urllib.request.urlretrieve(full_url, file_name)
    print('end download')
