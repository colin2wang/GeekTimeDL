# -*- coding: utf-8 -*-
import urllib
import os, sys
import re


# 'https://media001.geekbang.org/e8fd515b954144fabbde0510683e5c7a/2a5a540b9349499fb6d32f924b18e3fc-a0eec740caa5343d32395f5b476ea608-ld-00001.ts'
# %05d

urlSample = 'https://media001.geekbang.org/5dfff0b075174076b13cdc1173d949e0/7b9af238453c48ad9dab42fb796868c2-a6b9ef8acdfd37778d6421e61fc91da8-hd-00044.ts'

urlTmpl = re.sub(r'[0-9]{5}.ts', '%05d.ts', urlSample)

fileNameTmpl = 'QCon-%05d.ts'

for idx in range(1, 5000):
    url = urlTmpl % idx
    print url
    fileName = 'Videos\\' + fileNameTmpl % idx
    response = urllib.urlretrieve(url, fileName)
    headers = response[1].headers
    if 'application/octet-stream' not in headers[1]:
        os.remove(fileName)
        break


