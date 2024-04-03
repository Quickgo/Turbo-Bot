import pandas as pd

def DataReady(DataFrame):
    DataFrame.drop('symbol', axis = 1, inplace = True)
    DataFrame.index = pd.to_datetime(DataFrame.index)
    return DataFrame