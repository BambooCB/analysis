#!/usr/bin/env python3
import pandas as pd, pathlib
from wordcloud import WordCloud

root = pathlib.Path(__file__).resolve().parents[2] 
out  = root/'analysis'/'result'
out.mkdir(exist_ok=True, parents=True)

df = pd.read_csv(root / 'linux_mm_commits_all.csv')
df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')
df['Date'] = df['Date'].dt.tz_convert(None)

bug = df[df['Commit Message'].str.contains(r'fix|bug|oops',case=False,regex=True)]

bug.groupby(bug['Date'].dt.year).size().to_csv(out/'bug_yearly.csv')

WordCloud(width=800,height=400)\
  .generate(' '.join(bug['Commit Message']))\
  .to_file(out/'bug_wc.png')
print('✅ 生成 bug_yearly.csv & bug_wc.png')
