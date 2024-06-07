import pandas as pd
import numpy as np

def DataReady(DataFrame):
    DataFrame.drop('symbol', axis = 1, inplace = True)
    DataFrame.index = pd.to_datetime(DataFrame.datetime)
    DataFrame.drop('datetime', axis = 1, inplace = True)
    return DataFrame


def KijunSen(data, length):
    lowest_low = pd.Series(data["Low"].rolling(window=length).min())
    highest_high = pd.Series(data["High"].rolling(window=length).max())
    return (lowest_low + highest_high) / 2