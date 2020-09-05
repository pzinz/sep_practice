
import numpy as np
import pandas as pd
import pandas_datareader as web
import datetime as dt
start = dt.datetime(2015, 1, 1, 0, 0)
end = dt.datetime.now()
df = web.DataReader('MSFT', 'yahoo', start, end)
Symbol = 'High'
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop('High',axis='columns')
print(df.head())
