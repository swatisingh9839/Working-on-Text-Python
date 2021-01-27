import re
import keyword
keywordsList = keyword.kwlist
refListDic = {}
linecounter = 1
f = open(r"C:\swati\Uppsala University\Period 2 HT 2020\Programming in Python\codetext.txt","r+")
for line in f.readlines():
    line = re.sub(r'#.*','',line)
    wordList = re.findall(r'[a-zA-Z0-9]+',line)

    for w in wordList:
        if w in wordList:
            if w not in keywordsList and not (w.isdigit()):
                if w in refListDic:
                    refListDic[w].append(linecounter)
                else:
                    refListDic[w] = [linecounter]
    linecounter += 1

refList = sorted(refListDic.items())

print('Reference List : \n')
for l in refList:
 print(f'{l[0]}:{l[1]}\n')

