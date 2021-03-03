from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
import re
import string


def clearSenentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1]
    return sentence


def clearInput(content):
    content = content.upper()
    content = re.sub(r'\n|\[\d+\]', ' ', content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii', 'ignore')
    content = content.split('. ')
    return [clearSenentence(sentence) for sentence in content]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output


def getNgrams(content, n):
    content = clearInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngrams) for ngrams in getNgramsFromSentence(sentence, n)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return ngrams, ngrams_list

html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id':'mw-content-text'}).getText()
ngrams, nlist = getNgrams(content, 2)
print(ngrams)
print(nlist)