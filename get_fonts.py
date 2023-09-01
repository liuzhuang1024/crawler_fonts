# coding: utf-8
import requests
from chars import usualUniCode_3500
from uuid import uuid1
import os
import shutil
import psutil
import subprocess
import json
from typing import List

url = "https://ziti.51ifonts.com/build/build-font-file/?font_id={}&words={}&format=ttf&hex=1&hash="
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

step = 50
target_font_dir = "fonts/"

fontlists: List = json.load(open("fontList.json"))

for font in fontlists:
    font_id = font['id']
    font_name = font['title']
    if os.path.exists(f"{target_font_dir}/{font_name}.ttx"):
        print(f"Exists {font_name}. ID: {font_id}")
        continue
    fonts_tmp = f"{uuid1().hex}/"
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
        stat, output = subprocess.getstatusoutput(f"python merger.py {filelists} --output-file={target_font_dir}/{font_name}.ttf")
        print(f"{font_id}.ttx Done!")
    shutil.rmtree(fonts_tmp)
        