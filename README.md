# ML_Stock_Analysis
  - Introduction
 
    - After the Pandemic people started spending a lot more time researching and investing time and money into stocks and crypto-currency. We, as a team held a common interest in stocks and wanted to apply what we learnt to conduct some sort of analysis on stock data. 
The most idealistic use of machine learning in this scenario would be predicting the target stocks’ price on a daily basis, that would be a good indicator of the right price to buy/sell in order to optimize your investment. Unfortunately, there are a lot of external factors that affect the push and pull of the market making it impossible to give a solid figure or local maxima/minima on a graph to follow and produce that trend. 
So we dove into the options of exploring different technical analysis methods to apply to stock data. We planned to research the data we had and apply real market analysis techniques on a short-term basis to train our models to forecast a graph of some sort of trend for the near-future. 
 
  - Problem Definition and Algorithm 
 
    - Task Definition
    The ideal outcome of the task at hand is to predict the stock price of a target company on the following day. We chose a dataset from Kaggle considering all the company’s listed on the NASDAQ with a varying time period and ranging back to a couple of years. All the companies had the factors of Open price, Close price, High/Low of that day, the date and the volume of stocks sold. 
Formally the list of inputs into the model would be:
Name of Target Company
Start/End Date
Open and Close Price  
Daily High/Low Price
Volume of stocks sold
The problem to solve was creating a graph output that would match the trend as close as possible and based on the data our algorithm generates we predict the next day’s stock price.
 
 
 
    - Algorithm Definition 
      - We first Let the user input a company symbol listed on the NASDAQ index. This input is used to pull the data from the Yahoo API concurrently and assigns it in a dataframe format. After assigning a preset time period which we found to be the most accurate to predict the trend to 1 day in the future we considered, 2012-2020 for our dataset. We assigned 25 days as the time period to be imputed into the neural network and decided that stock market data from 2012-2020 be used as our training data. This data was fitted and transformed based on the ‘Adjusted Close’ Price.
We then split the Data to use in training the prediction algorithm and then had to produce a test set to verify our data to improve the model. We reshaped the data before feeding it into the neural net and converted to Numpy arrays of the correct sizes.

      - We chose a Neural Net to accomplish this task of predicting based on trends. Specifically we chose a LSTM (Long Short-Term Memory) type of neural net because it would consider feedback connections rather than just a feedword connections to process the sequence of trends being formed. We used a Dropout functionality to regularize our data and avoid extensive overfitting, this process accounts for situations when a trend is carried forward through layers and needs to be broken down. We found this process highly useful for our stock data and added them between the layers with a probability of ‘0.3’. We Included a Rectified Linear Unit Activation function(ReLU) in order to improve the performance of our algorithm and make it faster as the function considered a positive correlation of probabilities and disregarded a negative one, thus increasing the accuracy as it ran through the layers.

      - After this step, a test set was manually formed again from 2020 to the current date to predict this time period using our algorithm and compared it to the actual values we pulled from the API. This was further confirmation after the actual test set to verify whether the trends our model created matched the graph trends of the stock price. We produced a graph that mapped the real stock data vs our model to visualize the accuracy of the prediction. Finally, we repeated these steps for epochs of 1 to 50 and plotting their respective graphs as well. 
 
  - Experimental Evaluation 
    - Methodology:
  We decided to test how many epochs was the ideal number to most accurately predict the next day’s stock price. Our hypothesis was that accuracy would gradually increase as the number of epochs increased until overfitting occurred to where the accuracy would decrease. We ran a loop to iterate through 1 to 50 epochs and then fitted and tested the model accordingly. Each iteration was plotted with the stock price and what was predicted. The accuracy of the model was determined by the difference between predicted price and the actual price on the next day. These differences in price were also plotted with respect to epoch. Other alternatives to our project would be to test the optimal number of prediction days (how many days of stock prices does the model receive) or finding the optimal neural network architecture. 
 
  - Results 
    - We inculcated a visual aspect into our program to get feedback on how our model was performing in relation to actual stock prices and histories. The following figures will present the actual stock price of Facebook plotted against the price that our neural network predicted over a sample of different epochs.



    - The following figure presents the difference between the actual close price of Facebook on 5/7/2021 and the predicted stock price over different epochs. For example, if the close price of a stock was $100 and the predicted price was $90, then the graph below would plot $10 (as the difference) on its respective epoch. It is clear in this figure that around 22 epochs would be the ideal number for our neural network to provide the most accurate price prediction. 

 
  - Discussion 
    - It seems that our initial hypothesis was correct in that the accuracy of the predicted stock price gradually improved over an increased number of epochs, until it reached 22 epochs where it began sharply decreasing in accuracy. The primary issue with this model is that, even though it fits rather well, we aren’t doing a classification task. Slightly under predicting and over predicting close price produce very different results if we were to use this model for stock trades. In general, it seemed that our model generally underpredicts stock prices and lags stock price movements. If this model was used for practical application, this would imply that many of your stock trades would either be simply incorrect or achieve significantly diminished results. 
 
  - Related Work
    - Another way we could have structured our model was, instead of predicting a specific stock price, to try and predict either upward or downward movement within a certain time frame. This way, it becomes a classification task rather than what we did in our project. However, using the XGBoost algorithm, the researcher failed to achieve a higher accuracy rate than simply choosing higher or lower at random. His results were not statistically significant enough to warrant his algorithm for practical use. 
 
  - Future Work
    - As mentioned previously in the discussion section, the major flaw in our model is that it has no real predictive power. In order to improve, we think that it would be productive to experiment with the neural network architecture and the number of prediction days imputed into the model. Generalizing the model to incorporate a bigger dataset of data and maybe even include more companies into the model would possibly increase the predictive accuracy - as some stocks may be easier to predict than others. 
 
  - Conclusion 
    - We learned about a lot through the process of analyzing different technical analysis methods incorporated into the formation of our models. We accomplished the task of finding a general technique of using the data present to us analyze it and generate a method to predict the chosen stock prices one day into the future. The researching and learning process gave us a lot of insight into the process of generalizing and predictively analyzing stock trends. 
We did not achieve our goal of predicting stock market prices per say. However, with the improvements mentioned in the previous section as well as continued monitoring of new machine learning innovations, I believe this task can be successfully achieved. We had a lot of ideas to build off this project itself and this could be used as the basic outlying structure of a much more detailed algorithm. 

  - Bibliography 
    - https://towardsdatascience.com/what-happened-when-i-tried-market-prediction-with-machine-learning-4108610b3422
    - https://school.stockcharts.com/doku.php?id=overview:technical_analysis
    - https://core.ac.uk/download/pdf/52104888.pdf
    - https://www.analyticsvidhya.com/blog/2020/10/reinforcement-learning-stock-price-prediction/
    - https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
    - https://riptutorial.com/pandas/example/6232/datareader-basic-example--yahoo-finance-

