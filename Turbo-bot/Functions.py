import pandas as pd

df = pd.read_csv("/home/zymantas/Desktop/Training_data/5minData/ATOMUSDT5min.csv", index_col = 0)

def DateTime(df):
    df.index = pd.to_datetime(df.index)
    return df