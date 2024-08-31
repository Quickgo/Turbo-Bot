import pandas as pd
import numpy as np

from tvDatafeed import TvDatafeed, Interval

def DataReady(DataFrame):
    DataFrame.drop('symbol', axis = 1, inplace = True)
    DataFrame.index = pd.to_datetime(DataFrame.datetime)
    DataFrame.drop('datetime', axis = 1, inplace = True)
    return DataFrame


def KijunSen(data, length):
    lowest_low = pd.Series(data["Low"].rolling(window=length).min())
    highest_high = pd.Series(data["High"].rolling(window=length).max())
    return (lowest_low + highest_high) / 2

def GetData():
    tv = TvDatafeed()
    Data = tv.get_hist("ATOMUSDT.P", "BYBIT", interval=Interval.in_5_minute, n_bars=50000, extended_session=True)
    Data.to_csv("/home/porsche/Desktop/Training_data/5minData/ATOMUSDT5min.csv")