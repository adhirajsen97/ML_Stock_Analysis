import pandas as pd
import os, requests;
from os import walk
from pathlib import Path
import yfinance as yf


path = Path(__file__).parents[2]




def main():

	#set path locally
	stock_path = str(path) + "/StockData/stocks/"

	#Get a list of files from stocks directory
	stock_names = os.listdir(stock_path)

	
	

	# read metadata csv
	meta = pd.read_csv(str(path) + "/StockData/symbols_valid_meta.csv")
	#print(meta)   # print Metadata head


	comp_acronym = meta["Symbol"].tolist()

	'''
	stocklist = pd.DataFrame()
	for i in comp_acronym:

		#print( str(comp_acronym.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)
		
		file = str(i) + ".csv"
		if file in stock_names:
			stock = pd.read_csv(stock_path+file)
		else:
			continue
			

		if len(stock) == 0 : 
			None
		else:
			stock["Name"] = i 
			stocklist = stocklist.append(stock, sort = False)
	
	print(stocklist.head())
	'''

	
	'''
	# create pd series of dates specified from start to end
	start_date = '2010-01-22'
	end_date = '2020-01-26'
	dates = pd.date_range(start_date, end_date)

	#create a df with index start and end date specified
	df = pd.DataFrame(index=dates)
	#print(df)
	'''





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