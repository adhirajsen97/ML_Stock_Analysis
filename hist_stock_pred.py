import pandas as pd
import numpy as np
from datetime import datetime, date
from pathlib import Path
import os

from sklearn.model_selection import train_test_split

path = Path(__file__).parents[2]
stock_path = str(path) + "/StockData/stocks/"

#Get a list of files from stocks directory
stock_names = os.listdir(stock_path)

# start date should be within 5 years of current date according to iex API we have used
# The more data we have, the better results we get!

start = datetime(2016, 1, 1)
end = date.today()
# use your token in place of token which you will get after signing up on IEX cloud
# Head over to https://iexcloud.io/ and sign-up to get your API token
df = pd.DataFrame()
df = pd.read_csv(str(stock_path) + "AAPL.csv")

prices = df[df.columns]
print(prices)
prices.reset_index(level=0, inplace=True)
prices["timestamp"] = pd.to_datetime(prices["Date"])
prices = prices.drop(['Date'], axis=1)


dataset = prices.values
X = dataset[:,1].reshape(-1,1)
Y = dataset[:,0:1]

validation_size = 0.15
seed = 7

X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size, random_state=seed)
