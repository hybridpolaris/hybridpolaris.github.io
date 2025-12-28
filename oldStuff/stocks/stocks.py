import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from matplotlib.widgets import Button

# Parameters for simulation
S0 = 100        # Initial stock price
mu = 0.05       # Drift (expected return)
sigma = 0.2     # Volatility (standard deviation of returns)
T = 1           # Time period (1 year)
dt = 1/252      # Time step (daily steps, assuming 252 trading days per year)
n = int(T / dt) # Number of time steps (252 for 1 year)
t = np.linspace(0, T, n)  # Time array

# Initialize arrays for stock prices and OHLC data
S = np.zeros(n)  # Array to store stock prices
S[0] = S0  # Set the initial price
ohlc = []

# Function to simulate the next candlestick
def add_candle(event):
    i = len(ohlc)
    if i < n:
        Z = np.random.normal(0, 1)  # Random noise
        # Generate stock prices based on GBM formula
        S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

        # Create random open, high, low, and close values around the price
        open_price = S[i-1] * (1 + np.random.normal(0, 0.01))  # Small deviation for open
        close_price = S[i] * (1 + np.random.normal(0, 0.01))  # Small deviation for close
        high_price = max(open_price, close_price) * (1 + np.random.normal(0, 0.02))  # High
        low_price = min(open_price, close_price) * (1 - np.random.normal(0, 0.02))   # Low
        ohlc.append([t[i], open_price, high_price, low_price, close_price])

        # Convert ohlc data into a pandas DataFrame for mplfinance
        ohlc_df = pd.DataFrame(ohlc, columns=['Date', 'Open', 'High', 'Low', 'Close'])

        # Convert 'Date' column to datetime and set as index
        ohlc_df['Date'] = pd.to_datetime(ohlc_df['Date'], unit='D', origin=pd.Timestamp('2025-01-01'))
        ohlc_df.set_index('Date', inplace=True)

        # Clear the previous plot and plot the updated data
        ax.clear()
        mpf.plot(ohlc_df, type='candle', style='charles', title="Simulated Candlestick Chart", ylabel='Stock Price', ax=ax)
        plt.draw()

# Set up the figure and axes for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Initial empty plot
mpf.plot(pd.DataFrame(columns=['Open', 'High', 'Low', 'Close']), type='candle', style='charles', title="Simulated Candlestick Chart", ylabel='Stock Price', ax=ax)

# Add a button for generating new candles
ax_button = plt.axes([0.8, 0.01, 0.1, 0.05])  # position of the button
button = Button(ax_button, 'Add Candle')
button.on_clicked(add_candle)

plt.show()
