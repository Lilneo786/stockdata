# stockdata
I wanted to check how many times in the last 10 years+ S&amp;P has been up, down, or flat in the first quarter of the year so I created this to help me out and save me alot of time.

I developed a Python script that allows users to download historical data for the S&P 500 index for specified quarters and years. The script utilizes yfinance library for fetching financial market data, and pandas library. The user can select specific quarters (Q1, Q2, Q3, Q4) and years (starting from 1980 up to the current year) or choose to download data for all available quarters and years. The script then processes this data and exports it to an Excel spreadsheet for easy viewing and analysis.

Key Features
User Input for Data Selection:

Users can specify the year and quarter for which they want the S&P 500 data.
Options include selecting individual years and quarters or choosing 'all' to fetch data for all years and quarters from 2013 to the present year.
Data Fetching:

The script uses yfinance to download historical data for the S&P 500 Index (ticker: ^GSPC).
It retrieves data for each selected quarter of each selected year, focusing on the 'Close' price of the index.
Data Aggregation and Export:

The data is aggregated and organized into a pandas DataFrame.
The DataFrame is then exported to an Excel file, making it easy to view, share, and analyze.
Dynamic Year Handling:

The script automatically adjusts to include data up to the current year, ensuring it remains relevant and up-to-date without manual changes.
Executable File Creation:

Using PyInstaller, we converted the Python script into a standalone executable file.
This executable allows users to run the script without needing a Python environment, making it more accessible for non-programmers.
How to Use the Executable
Run the Executable: Users simply run the executable file. On Windows, this is done by double-clicking the .exe file.

Input Desired Parameters: Upon running, the script prompts for the year and quarter. Users can input specific years and quarters or type 'all' for fetching data across all years and quarters.

Excel File Generation: After the data is fetched and processed, the script automatically generates an Excel file (sp500_data.xlsx) with the historical S&P 500 data organized by the selected quarters and years.

Applications
Financial Analysis: Useful for financial analysts, investors, or anyone interested in stock market trends, particularly in analyzing the historical performance of the S&P 500 index.
Educational Purposes: Can be used for educational demonstrations in finance, economics, or data analysis classes.
Personal Finance Tracking: Individuals tracking their investments or studying market trends can use this tool for personal finance management.
Technical Requirements
The executable is platform-specific and currently built for Windows.
No Python installation is required to run the executable.
Conclusion
This tool is designed to make financial data more accessible and easier to analyze, catering to both individuals with and without programming backgrounds. Its user-friendly interface and Excel output format make it a practical utility for a variety of financial analysis tasks.

The .exe is in the DIST folder and the rest of the code is attached. When you execute the ,exe file it'll ask you for the Year and Quarter you'd like to extract data and then it'll extract that data from Yahoo finance and convert the data into an Excel sheet named "sp500_data.
