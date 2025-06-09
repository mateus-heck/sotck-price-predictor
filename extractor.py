import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    """
    Downloads historical stock data for a given ticker symbol between specified dates.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    df = pd.DataFrame(stock_data)
    if df.empty:
        print(f"No data found for {ticker} between {start_date} and {end_date}.")
    else:
        df.to_csv('PETR4_SA.csv', index=True)
        return "Data downloaded successfully."
     
def __main__():
    ticker = 'PETR4.SA'
    start_date = '2020-01-01'
    end_date = '2025-05-30'
    download_stock_data(ticker, start_date, end_date)
    pass