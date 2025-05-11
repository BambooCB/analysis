#!/usr/bin/env python3
import pandas as pd, pathlib, re, bs4
root = pathlib.Path(__file__).resolve().parents[2] 
rows = []
for html in (root/'html').rglob('*.html'):
    m = re.search(r'v([^_/]+)_(v[^/]+)/mm', str(html))
    if not m: continue
    prev, curr = m.groups()
    soup = bs4.BeautifulSoup(open(html,'rb'),'html.parser')
    ins  = len(soup.select('span.diff_add'))
    delt = len(soup.select('span.diff_sub'))
    rows.append({'prev':prev,'curr':curr,'file':html.stem,'ins':ins,'del':delt})
pd.DataFrame(rows).to_csv(root/'analysis'/'result'/'html_file_churn.csv', index=False)
print('✅ 生成 html_file_churn.csv')
