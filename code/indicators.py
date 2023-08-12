import numpy as np
def calc_MA(data, period: int = 7) -> np.ndarray:
    #Calculates the Moving Average for the closing data for the given period (in number of days).
    moving_average = np.full(len(data), np.nan)
    day_idx = period #Skipping the first n days for Moving Averages

    while(day_idx < len(data)):
        closing_sums = np.sum(data.iloc[day_idx-period:day_idx])
        moving_average[day_idx] = closing_sums/period
        day_idx = day_idx + 1

    return moving_average

def rsi(prices, periods=14, ema = True):
    """
    Returns a pd.Series with the relative strength index.
    """
    close_delta = prices.diff()
    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    if ema == True:
	    # Use exponential moving average
        ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
        ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(window = periods, adjust=False).mean()
        ma_down = down.rolling(window = periods, adjust=False).mean()
        
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    return rsi