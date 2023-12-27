import yfinance as yf
import pandas as pd
from datetime import datetime  # Make sure this line is included

def download_sp500_data(start_date, end_date):
    """Download S&P 500 data for a given date range."""
    sp500_ticker = "^GSPC"
    return yf.download(sp500_ticker, start=start_date, end=end_date)

def get_quarter_dates(year, quarter):
    """Get start and end dates for a specific quarter of a given year."""
    quarters = {
        "Q1": (f"{year}-01-01", f"{year}-03-31"),
        "Q2": (f"{year}-04-01", f"{year}-06-30"),
        "Q3": (f"{year}-07-01", f"{year}-09-30"),
        "Q4": (f"{year}-10-01", f"{year}-12-31"),
    }
    return quarters[quarter]

# Get the current year
current_year = datetime.now().year

# User input for year and quarter
year_input = input("Enter the year (YYYY) or 'all' for all years: ")
quarter_input = input("Enter the quarter (Q1, Q2, Q3, Q4) or 'all' for all quarters: ")

# Define years and quarters
years = range(2013, current_year + 1) if year_input.lower() == 'all' else [int(year_input)]
quarters = ['Q1', 'Q2', 'Q3', 'Q4'] if quarter_input.lower() == 'all' else [quarter_input]

# Fetching and storing data
sp500_data = {}
for year in years:
    for quarter in quarters:
        start_date, end_date = get_quarter_dates(year, quarter)
        data = download_sp500_data(start_date, end_date)
        sp500_data[f"{year} {quarter}"] = data['Close']

# Convert to DataFrame
df = pd.DataFrame(sp500_data)

# Export to Excel
df.to_excel("sp500_data.xlsx")
