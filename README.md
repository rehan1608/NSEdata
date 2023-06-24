**Terminal Commands:-**  
pip install pandas  
pip install yfinance  
pip install matplotlib  
pip install mpl-finance  


**Summary:-**  
	  This Python script aims to extract historical stock data for a given symbol from the National Stock Exchange (NSE) of India using the yfinance library and visualize the stock's performance over a selected period as a candlestick chart using matplotlib and mpl_finance. The script comprises three main steps: Data Extraction, Data Processing and Data Visualization.  

**Functions:-**  

**1-Data Extraction**  
	In the Data Extraction step, the extract_historical_data() function is responsible for fetching the stock data using the yf.download() function from the yfinance library. It takes the stock symbol, start date, and end date as input, and returns a Pandas DataFrame containing the historical stock data.  

**2-Data Processing**  
	The Data Processing step involves calculating the average daily trading volume for the extracted stock data. The calculate_average_volume() function adds an 'Average Volume' column to the DataFrame, representing the rolling average of the volume over a window size of 5.  

**3-Data Visualization**  
	In the Data Visualization step, the visualize_candlestick_chart() function takes the processed stock data and symbol as input. It prepares the data for the candlestick chart, sets up the chart axes, formats the x-axis ticks, and plots the candlestick chart using the candlestick_ohlc() function.  

**Error-Handling:-**  
	The script is designed to handle errors during data extraction and provides appropriate error messages. Additionally, comments are included throughout the script to explain the purpose of each function and provide clarity to the code.  

**Usage Example:**  
		$ python stockData.py

		Enter the stock symbol: TCS
		Enter the starting date (YYYY-MM-DD): 2022-01-01


**Challenges I ancountered:-**

1- I wasn't able to get the data of the stock I was entring and I was getting the error again and again that the stock doesn't exist, I googled it but didn't get any help than I moved to https://finance.yahoo.com/quote/%5ENSEI/components/ and noticed that every stock symbol contains ".NS" in last so I modified the script accordingly.

2- I was asking the user to enter the starting date but after this I wasn't able to calculate one year after that so I moved to https://docs.python.org/3/library/datetime.html and noticed that datetime module has inbuilt object "timedelta()" to calculate the time duration and fixed it.

3- I was getting the dark blacke space below the x-axis and it was creating the confusion for, I tried to overcome it but couldn't, so I moved to ChatGpt(openAI AI tool) and came to know that it was because of the overlapping of the date labels, To fix this issue, I adjust the x-axis tick placement and rotation to make the labels more readable.

