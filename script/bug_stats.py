#!/usr/bin/env python3
import pathlib, re
import pandas as pd, pathlib
from wordcloud import WordCloud
from _util import load_commits_csv, root

out = root/'analysis'/'result'; out.mkdir(parents=True, exist_ok=True) 

df  = load_commits_csv()

bug = df[df['Commit Message'].str.contains(r'fix|bug|oops', flags=re.I, regex=True)]

bug.groupby(bug['Date'].dt.year).size().to_csv(out/'bug_yearly.csv')

WordCloud(width=800,height=400)\
  .generate(' '.join(bug['Commit Message']))\
  .to_file(out/'bug_wc.png')
print('✅ 生成 bug_yearly.csv & bug_wc.png')
