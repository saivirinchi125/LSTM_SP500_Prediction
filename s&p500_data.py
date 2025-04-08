!pip install yfinance pandas

import yfinance as yf
import pandas as pd

# Specify date range
start_date = '2018-04-07'   # YYYY-MM-DD format
end_date = '2023-04-07'     # YYYY-MM-DD format

# Fetch S&P 500 data for the specified date range
ticker = "^GSPC"
data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Display first few rows
print(data.head())

# Save data to CSV file locally
data.to_csv('/content/SP500_data.csv')
