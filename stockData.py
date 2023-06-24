import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Step 1: Data Extraction
def extract_historical_data(symbol, start_date, end_date):
    """
    Extracts historical stock data for the specified symbol and date range using the yfinance library.

    Args:
        symbol (str): Stock symbol.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.

    Returns:
        pd.DataFrame: DataFrame containing the extracted historical stock data.
    """
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print("An error occurred during data extraction:", str(e))
        return None

# Step 2: Data Processing
def calculate_average_volume(stock_df):
    """
    Calculates the average daily trading volume for the stock.

    Args:
        stock_df (pd.DataFrame): DataFrame containing the stock data.

    Returns:
        pd.DataFrame: DataFrame with an additional 'Average Volume' column.
    """
    stock_df['Average Volume'] = stock_df['Volume'].rolling(window=5).mean()
    return stock_df

# Step 3: Data Visualization
def visualize_candlestick_chart(stock_df, symbol):
    """
    Visualizes the stock's performance over the selected period as a candlestick chart.

    Args:
        stock_df (pd.DataFrame): DataFrame containing the stock data.
        symbol (str): Stock symbol.
    """
    
    # Prepare the data for the candlestick chart
    stock_df['Date'] = mdates.date2num(stock_df.index.to_pydatetime())
    ohlc = stock_df[['Date', 'Open', 'High', 'Low', 'Close']]

    # Create the candlestick chart
    fig, ax = plt.subplots()

    # Adjust the x-axis tick placement and rotation
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Price')
    symbol=symbol[:-3]
    plt.title('Candlestick Chart for {}'.format(symbol))

    # Display the chart
    plt.show()

# Prompt the user for stock symbol input
symbol = input("Enter the stock symbol: ").upper()+".NS"

while True:
    # Prompt the user for the starting date
    start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        # Calculate the one year after as the end date
        end_date = start_date + timedelta(days=365)
        end_date_str = end_date.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in the format 'YYYY-MM-DD'.")
        continue

    # Extract historical data
    stock_df = extract_historical_data(symbol, start_date_str, end_date_str)

    if stock_df is not None and not stock_df.empty:
        # Stock data exists, visualize the candlestick chart
        visualize_candlestick_chart(stock_df, symbol)
        break
    else:
        print("Stock '{}' doesn't exist or data is not available for the specified date range. Please enter a valid stock symbol and starting date.".format(symbol))
        symbol = input("Enter the stock symbol: ").upper()+".NS"
