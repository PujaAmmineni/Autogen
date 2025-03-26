# filename: stock_price_chart_google_amazon.py
import yfinance as yf
import matplotlib.pyplot as plt

# Retrieve historical stock price data for Google and Amazon
google_data = yf.Ticker("GOOGL").history(period="1mo")
amazon_data = yf.Ticker("AMZN").history(period="1mo")

# Plot the stock price changes for both companies
plt.figure(figsize=(12, 6))
plt.plot(google_data.index, google_data['Close'], label='Google (GOOGL)')
plt.plot(amazon_data.index, amazon_data['Close'], label='Amazon (AMZN)')
plt.title('Stock Price Changes - Google vs. Amazon')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()