# coding: utf-8
import requests
from chars import usualUniCode_3500
from uuid import uuid1
import os
import shutil
import psutil
import subprocess

url = "https://ziti.51ifonts.com/build/build-font-file/?font_id={}&words={}&format=ttf&hex=1&hash="
step = 50
fonts_tmp = "fonts_tmp/"
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

for font_id in [5458]:
    shutil.rmtree(fonts_tmp)
    os.mkdir(fonts_tmp)
    for index in range(0, len(usualUniCode_3500), step):
        print("Font ID:", font_id, "Index: ", index)
        tmp_url = url.format(font_id, ",".join([hex(i).strip('0x') for i in usualUniCode_3500[index:index+step]]))
        respone = requests.get(tmp_url, headers=headers)
        if not respone.ok:
            print(f"{font_id}.ttx Faild!")
            break
        open(fonts_tmp + uuid1().hex + '.ttf', 'wb').write(respone.content)
    else:
        print(f"{font_id}.ttx Processing ...")
        filelists = " ".join([root + "/" + file for root, _, files in os.walk(fonts_tmp) for file in files])
        stat, output = subprocess.getstatusoutput(f"python merger.py {filelists} --output-file=fonts/{font_id}.ttf")
        print(f"{font_id}.ttx Done!")