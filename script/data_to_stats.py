#!/usr/bin/env python3
import pandas as pd, pathlib
from _util import load_commits_csv, root

out_dir = root/'analysis'/'result'; out_dir.mkdir(parents=True, exist_ok=True)
df,first_date = load_commits_csv()

release = {
    'v2.6.39':'2011-05-19','v3.0':'2011-07-22','v3.13':'2014-01-20',
    'v4.0':'2015-04-12','v4.19':'2018-10-22','v5.4':'2019-11-24',
    'v5.10':'2020-12-13','v5.17':'2022-03-20'}
release = {'v2.x':'2000-01-01', **release}
release = {k: pd.to_datetime(v) for k,v in release.items()}
tags    = list(release)

def locate(ts):
    for p,c in zip(tags[:-1],tags[1:]):
        if release[p] <= ts < release[c]:
            return f'{p}->{c}'
    return None

df['range'] = df['Date'].map(locate)
out = root/'analysis'/'result'/'mm_change_summary.csv'
(df.groupby('range')
   .agg(commits=('Date','size'),
        insertions=('Insertions','sum'),
        deletions=('Deletions','sum'))
 ).to_csv(out)
print('✅ 生成', out)
