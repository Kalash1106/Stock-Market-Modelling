import pandas as pd
import matplotlib.pyplot as plt 
from indicators import calc_MA, rsi


if __name__ == "__main__":
    
    filepath = "../sensex_data.csv"
    raw_data = pd.read_csv(filepath)
    rsi = rsi(raw_data['Close'])
    
    #Plotting
    plt.plot(rsi)
    plt.title("Indicator")
    plt.xlabel("Day")
    plt.ylabel("RSI Index")
    plt.show()