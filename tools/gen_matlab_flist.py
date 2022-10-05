import requests
from bs4 import BeautifulSoup


# -- 爬取网页
# FUNCTION_LIST_URL = 'http://127.0.0.1:4567/language-fundamentals.html'
# r = requests.get(FUNCTION_LIST_URL)
# if r.status_code != 200:
#     print(f'[error] status_code={r.status_code}')
#     exit(-r.status_code)

HTML_FILE_LIST = [
  'language-fundamentals.html',
  'data-import-and-analysis.html',
  'mathematics.html',
  'graphics.html',
  'programming-and-data-types.html',
  'gui-development.html',
  'software-development.html',
  'external-language-interface.html',
  'desktop-tools-and-development-environment.html',
]  # HTML_FILE_LIST


raw_html = None
fname = HTML_FILE_LIST[0]
with open(f'html_input/{fname}', 'r', encoding='utf-8') as f:
    raw_html = f.read()

soup = BeautifulSoup(raw_html, 'html.parser')
# 类别名称
soup.select("#nav_siblings > li.active > a")[0].contents[1]
# 函数列表
soup.select("#reflist_content")
print(soup)
