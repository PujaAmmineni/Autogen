# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Retrieve historical stock price data for Meta and Tesla
meta_data = yf.Ticker("FB").history(period="1mo")
tesla_data = yf.Ticker("TSLA").history(period="1mo")

# Plot the stock price changes for both companies
plt.figure(figsize=(12, 6))
plt.plot(meta_data.index, meta_data['Close'], label='Meta (FB)')
plt.plot(tesla_data.index, tesla_data['Close'], label='Tesla (TSLA)')
plt.title('Stock Price Changes - Meta vs. Tesla')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()