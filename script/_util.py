# analysis/script/_util.py
import pandas as pd, pathlib

root = pathlib.Path(__file__).resolve().parents[2]   # ~/projects/Linux_Memorymanagement_Dataset

def load_commits_csv() -> pd.DataFrame:
    """读取 linux_mm_commits_all.csv，并返回 tz-naive 的 datetime 列"""
    df = pd.read_csv(root / 'linux_mm_commits_all.csv')

    # ① 先让 pandas 解析成统一的 UTC 时间戳
    df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')

    # ② 再去掉时区信息，得到 tz-naive datetime64[ns]
    df['Date'] = df['Date'].dt.tz_convert(None)

    return df,df['Date'].min()

