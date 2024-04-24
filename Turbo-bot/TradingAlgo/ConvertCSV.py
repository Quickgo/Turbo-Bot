import pandas as pd

def DataReady(DataFrame):
    DataFrame.drop('symbol', axis = 1, inplace = True)
    DataFrame.index = pd.to_datetime(DataFrame.datetime)
    DataFrame.drop('datetime', axis = 1, inplace = True)
    return DataFrame