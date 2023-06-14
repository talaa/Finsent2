import yfinance as yf
from datetime import datetime

def get_stock_data(Tick):
    #today = datetime.date.today()
    today = datetime.today().date()
    tick = yf.download(Tick, '2023-1-1', today)
    #remove the index from df tick 
    tick.reset_index(inplace=True)
    # Format data in the DataFrame
    tick['Open'] = tick['Open'].map('{:.2f}'.format)
    tick['High'] = tick['High'].map('{:.2f}'.format)
    tick['Low'] = tick['Low'].map('{:.2f}'.format)
    tick['Close'] = tick['Close'].map('{:.2f}'.format)
    tick['Adj Close'] = tick['Adj Close'].map('{:.2f}'.format)
    tick.sort_values('Date', ascending=False,inplace=True)
    co=yf.Ticker(Tick)
    print(co.info)
    
    
    
    
    return tick,co
