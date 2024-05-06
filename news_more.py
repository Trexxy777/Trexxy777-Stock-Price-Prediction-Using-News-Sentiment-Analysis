import requests
import json
from datetime import date, timedelta

# Replace with your actual API token
api_token = "HeriBE3gb4Izp5F7Zwt1Ra6TjuTj08ZssEMoCB5k"

# Set the base URL for the API request
base_url = "https://api.marketaux.com/v1/news/all?filter_entities=true&language=en&api_token={}"

def get_news_data(symbol, published_on):
  """Fetches news data for a specific symbol and date.

  Args:
      symbol: The stock symbol (e.g., TSLA)
      published_on: The date in YYYY-MM-DD format

  Returns:
      A list of dictionaries containing news article information.
  """
  url = base_url.format(api_token) + f"&symbols={symbol}&published_on={published_on}"
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.text)
    news = []
    for article in data["data"]:
      news.append({
          "title": article["title"],
          "description": article["description"],
          "sentiment_score": article["entities"][0]["sentiment_score"]
      })
    return news
  else:
    print(f"Error: {response.status_code} for symbol {symbol} on {published_on}")
    return []

# Get news data for the last 5 days
companies = ["TSLA", "AMZN", "AAPL", "ITC.NS", "TATASTEEL.NS"]
daily_news = {}
for day_offset in range(5):
  day = date.today() - timedelta(days=day_offset)
  published_on = day.strftime('%Y-%m-%d')
  for company in companies:
    company_news = get_news_data(company, published_on)
    daily_news.setdefault(published_on, {})[company] = company_news

# Print news for each day
for date, company_news in daily_news.items():
  print(f"News for {date}:")
  for company, news_list in company_news.items():
    print(f"\tCompany: {company}")
    if news_list:
      for article in news_list:
        print(f"\t\tTitle: {article['title']}")
        print(f"\t\tDescription: {article['description']}")
        print(f"\t\tSentiment Score: {article['sentiment_score']}")
        print("\t\t-" * 20)
    else:
      print("\t\tNo news found for this company on this date.")
  print("-" * 50)
