#!/usr/bin/env python3
import pandas as pd, matplotlib.pyplot as plt, pathlib
root = pathlib.Path(__file__).resolve().parents[2] 
df   = pd.read_csv(root/'analysis'/'result'/'mm_change_summary.csv')
plt.plot(df['range'], df['insertions']+df['deletions'], marker='o')
plt.xticks(rotation=45); plt.ylabel('Lines changed'); plt.tight_layout()
plt.savefig(root/'analysis'/'result'/'mm_churn.png')
print('✅ 生成 mm_churn.png')
