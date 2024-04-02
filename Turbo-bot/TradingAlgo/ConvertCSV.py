import pandas as pd
import numpy as np

df = pd.read_csv("/home/zymantas/Desktop/Training_data/5minData/ATOMUSDT5min.csv")

def DataReady(DataFrame):
    DataFrame.rename(columns = {'datetime' : 'timestamp'}, inplace = True)
    DataFrame.drop('symbol', axis = 1, inplace = True)
    print(DataFrame)
    return DataFrame