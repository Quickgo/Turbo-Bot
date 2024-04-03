import pandas as pd

df = pd.read_csv("/home/zymantas/Desktop/Training_data/5minData/ATOMUSDT5min.csv")

def DataReady(DataFrame):
    DataFrame.rename(columns = {'datetime' : 'timestamp'}, inplace = True)
    DataFrame.drop('symbol', axis = 1, inplace = True)
    DataFrame
    print(DataFrame)
    return DataFrame