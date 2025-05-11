#!/usr/bin/env python3
import pathlib, re, pandas as pd, bs4

root = pathlib.Path(__file__).resolve().parents[2]
out  = root/'analysis'/'result'; out.mkdir(parents=True, exist_ok=True)
rows = []

def count_plain(text):
    add = sum(1 for line in text.splitlines() if line.startswith('+') and not line.startswith('+++'))
    rem = sum(1 for line in text.splitlines() if line.startswith('-') and not line.startswith('---'))
    return add, rem

for html in (root/'html').rglob('*.html'):
    m = re.search(r'v([^_/]+)_(v[^/]+)/mm', str(html))
    if not m: continue
    prev, curr = m.groups()

    with open(html,'rb') as f:
        soup = bs4.BeautifulSoup(f,'html.parser')
    ins = len(soup.select('span.diff_add'))
    rem = len(soup.select('span.diff_sub'))

    # 若新版标签计数为 0，则退回纯文本行首 '+/-' 方式
    if ins == 0 and rem == 0:
        ins, rem = count_plain(soup.get_text())

    rows.append({'prev':prev,'curr':curr,'file':html.stem,'ins':ins,'del':rem})

pd.DataFrame(rows).to_csv(out/'html_file_churn.csv', index=False)
print('✅ html_file_churn.csv 更新完毕')

