import requests
import re
import json
import selenium
from selenium.webdriver import ChromeOptions, Chrome, ActionChains
from selenium.webdriver.common.by import By
from typing import List

def use_get_methods():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://ifonts.com/"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode()
    return content

options = ChromeOptions()
browser = Chrome(options)

url = "https://ifonts.com/font-list?most=5&type_id=6"
browser.get(url)

fontlists = []
while True:
    content = browser.page_source
    fontlist = re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', content)[0]
    fontlist = json.loads(fontlist)
    fontlist = fontlist['props']['pageProps']['pageData']['fontList']
    fontlists.extend(fontlist)
    next = browser.find_elements(By.CLASS_NAME, 'MuiPaginationItem-page')
    if not next or next[-2].get_attribute('tabindex') != '0':
        break
    ActionChains(browser).click(next[-2]).perform()
    
json.dump(fontlists, open('fontList.json', 'w'), ensure_ascii=False)