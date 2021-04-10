import pandas as pd
import os
from os import walk

#set paths
path = os.getcwd()
stocks_path = path + "/StockData/stocks/"

# read all csv file names from stocks folder
_, _, stock_names = next(walk(stocks_path))

# read metadata csv
meta = pd.read_csv(path + "/StockData/symbols_valid_meta.csv")
print(meta.head(5))   # print Metadata head



# create pd series of dates specified from start to end
start_date = '2010-01-22'
end_date = '2020-01-26'
dates = pd.date_range(start_date, end_date)

#create a df with index start and end date specified
df = pd.DataFrame(index=dates)
#print(df)


'''
df = df.join(join_stock_data(stocks_path, stock_names[0]))
def join_stock_data(path, filename):
	df_stock = pd.read_csv(path+filename)
	return df
for symbol in stock_names:
	df_temp = pd.read_csv('StockData/stocks/{}'.format(symbol), index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"], na_values=['nan'])
	df = df.join(df_temp, how = 'inner', lsuffix = symbol)
'''