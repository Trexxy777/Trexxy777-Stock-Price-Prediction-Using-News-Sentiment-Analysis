import requests
import json
import matplotlib.pyplot as plt


# Replace with your actual API key
api_key = 'WLHRXAMCDX8TAHGA'

# Construct the API URL
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey={api_key}"

# Send the API request (assuming allowed by terms of service)
response = requests.get(url)

# Process the response (assuming successful request)
if response.status_code == 200:
    data = response.json()  # Assuming JSON response format

    # Extract closing and opening prices as in the previous code snippet
    closing_prices = []
    opening_prices = []
    for timestamp, price_data in data["Time Series (5min)"].items():
        closing_prices.append(float(price_data["4. close"]))
        opening_prices.append(float(price_data["1. open"]))

    # Print the results
    print("Closing Prices:", closing_prices[0:5])
    print("Opening Prices:", opening_prices[0:5])

else:
    print("Error:", response.status_code)

api_token = "o8BhFNrmfsrQVKFnadzlnQ5sSfraWhOIw9W3diAD"

published_on = "2024-04-26"


def get_news_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        sentiment_scores = []
        for article in data["data"]:
            sentiment_scores.append(article["entities"][0]["sentiment_score"])
        return sentiment_scores
    else:
        print("Error:", response.status_code)
        return []

scoreList = []
def print_sentiment_scores(symbol, sentiment_scores,scoreList):
    print(f"\nSentiment Scores for {symbol} on {published_on}:")
    for score in sentiment_scores:
        print(score)
        scoreList.append(score)


tesla_news = get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=TSLA&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")

print_sentiment_scores("Tesla", tesla_news, scoreList)
print(scoreList)
multiplied_list = [value * 1000 for value in scoreList]

plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
ax1 = plt.subplot()
ax2 = ax1.twinx()

ax1.plot(closing_prices, label='Closing Price', color='blue')
ax1.plot(opening_prices, label='Opening Price', color='green')
#ax1.plot(multiplied_list, label='Sentiment Score', color='red', linestyle='--')

plt.title(f'Sentiment Score, Opening & Closing Price for TSLA on {published_on}')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
