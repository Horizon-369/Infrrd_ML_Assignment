# Import necessary libraries
import yfinance as yf

# in order to specify start date and 
# end date we need datetime package
import datetime
 
# startDate , as per our convenience we can modify
startDate = datetime.datetime(2023, 10, 18)
 
# endDate , as per our convenience we can modify
endDate = datetime.datetime(2024, 10, 19)

ticker = 'NVDA'
stock_data = yf.Ticker(ticker)
 
# pass the parameters as the taken dates for start and end
data = stock_data.history(start=startDate, end=endDate)