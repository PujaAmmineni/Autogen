# filename: stock_price_chart_microsoft_apple.py
import yfinance as yf
import matplotlib.pyplot as plt

# Retrieve historical stock price data for Microsoft and Apple
microsoft_data = yf.Ticker("MSFT").history(period="1mo")
apple_data = yf.Ticker("AAPL").history(period="1mo")

# Plot the stock price changes for both companies
plt.figure(figsize=(12, 6))
plt.plot(microsoft_data.index, microsoft_data['Close'], label='Microsoft (MSFT)')
plt.plot(apple_data.index, apple_data['Close'], label='Apple (AAPL)')
plt.title('Stock Price Changes - Microsoft vs. Apple')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()