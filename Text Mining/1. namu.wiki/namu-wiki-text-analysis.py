# -*- coding: utf-8 -*-

import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os

# brew 로 설치된 chromedriver의 path (Mac)
# path = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(path)  # for Mac

# 크롤링할 사이트 주소를 정의합니다.
source_url = "https://namu.wiki/RecentChanges"

print(os.getcwd())

# 윈도우용 크롬 웹드라이버 실행 경로 (Windows)
excutable_path = "D:\\Git\\bigdata\\utils\\WebDriver\\chromedriver.exe"

# 사이트의 html 구조에 기반하여 크롤링을 수행합니다.
driver = webdriver.Chrome(executable_path=excutable_path)  # for Windows
driver.get(source_url)
req = driver.page_source
soup = BeautifulSoup(req, "html.parser")
contents_table = soup.find_all(name="table")
print(contents_table)
table_body = contents_table.find(name="tbody")
table_rows = table_body.find_all(name="tr")

# a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.
page_url_base = "https://namu.wiki"
page_urls = []
for index in range(0, len(table_rows)):
    first_td = table_rows[index].find_all("td")[0]
    td_url = first_td.find_all("a")
    if len(td_url) > 0:
        page_url = page_url_base + td_url[0].get("href")
        if "png" not in page_url:
            page_urls.append(page_url)

# 중복 url을 제거합니다.
page_urls = list(set(page_urls))
for page in page_urls[:5]:
    print(page)

# 크롤링에 사용한 브라우저를 종료합니다.
driver.close()

# driver = webdriver.Chrome(path)  # for Mac
driver = webdriver.Chrome(executable_path=excutable_path)  # for Windows
driver.get(page_urls[0])
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
contents_table = soup.find(name="article")
title = contents_table.find_all('h1')[0]
category = contents_table.find_all('ul')[0]
content_paragraphs = contents_table.find_all(name="div", attrs={"class":"wiki-paragraph"})
content_corpus_list = []

for paragraphs in content_paragraphs:
    content_corpus_list.append(paragraphs.text)
content_corpus = "".join(content_corpus_list)

print(title.text)
print("\n")
print(category.text)
print("\n")
print(content_corpus)

# 크롤링에 사용한 브라우저를 종료합니다.
driver.close()



# Copyright (c) 2019 [윤기태]
# https://github.com/yoonkt200/python-data-analysis
# MIT License