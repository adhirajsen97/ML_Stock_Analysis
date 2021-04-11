import pandas as pd
import os, requests;
from os import walk
from pathlib import Path

find = Path('symbols_valid_meta.csv')
path = find.parent.absolute()
path = str(path) + "/StockData/"





def main():

	

	#set path locally
	stock_path = path + "stocks/"
	print(stock_path)

	# read all csv file names from stocks folder
	_, _, stock_names = next(walk(stock_path))
	

	# read metadata csv
	meta = pd.read_csv(path + "/StockData/symbols_valid_meta.csv")
	print(meta.head(5))   # print Metadata head

	comp_acronym = meta["Symbol"].tolist()

	# create pd series of dates specified from start to end
	start_date = '2010-01-22'
	end_date = '2020-01-26'
	dates = pd.date_range(start_date, end_date)

	#create a df with index start and end date specified
	df = pd.DataFrame(index=dates)
	#print(df)






if __name__ == "__main__":
	main()


	'''
	df = df.join(join_stock_data(stocks_path, stock_names[0]))
	def join_stock_data(path, filename):
		df_stock = pd.read_csv(path+filename)
		return df
	for symbol in stock_names:
		df_temp = pd.read_csv('StockData/stocks/{}'.format(symbol), index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"], na_values=['nan'])
		df = df.join(df_temp, how = 'inner', lsuffix = symbol)
	'''