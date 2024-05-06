import requests
import json
from jinja2 import Template

# Replace with your actual API token
api_token = "VQ2v5vLGUyMcFdTn9wBSNNnBoeL2uwHBARvqwVQP"

published_on = "2024-05-03"



def get_news_data(url):
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
    print("Error:", response.status_code)
    return []

def generate_news_html(news_data):
  html = ""
  for article in news_data:
    html += f"""
    <div class="news-item">
      <h3>{article["title"]}</h3>
      <p>{article["description"]}</p>
      <p>Sentiment Score: {article["sentiment_score"]}</p>
    </div>
    """
  return html

tesla_news = get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=TSLA&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")
amazon_news = get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=AMZN&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")
apple_news =  get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=AAPL&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")
itc_news = get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=ITC.NS&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")
tata_news = get_news_data(f"https://api.marketaux.com/v1/news/all?symbols=TATASTEEL.NS&filter_entities=true&language=en&published_on={published_on}&api_token={api_token}")
tesla_news_html = generate_news_html(tesla_news)
amazon_news_html = generate_news_html(amazon_news)
apple_news_html = generate_news_html(apple_news)
itc_news_html = generate_news_html(itc_news)
tata_news_html = generate_news_html(tata_news)
print("111111111111111",tesla_news_html)

# Load the HTML template and render it with the generated news HTML
with open("templates/about.html", "r") as template_file:
  template = Template(template_file.read())
  rendered_html = template.render(name = "Tesla",tesla_news_html=tesla_news_html, current_date=published_on)

# Write the rendered HTML to a new file (optional)
with open("templates/output_TSLA.html", "w") as output_file:
  output_file.write(rendered_html)

print("Generated news webpage: output_TSLA.html")

with open("templates/about.html", "r") as template_file:
  template = Template(template_file.read())
  rendered_html = template.render(name = "Amazon",amazon_news_html=amazon_news_html, current_date=published_on)

# Write the rendered HTML to a new file (optional)
with open("templates/output_AMZN.html", "w") as output_file:
  output_file.write(rendered_html)

print("Generated news webpage: output_AMZN.html")

with open("templates/about.html", "r") as template_file:
  template = Template(template_file.read())
  rendered_html = template.render(name = "Apple",apple_news_html=apple_news_html, current_date=published_on)

# Write the rendered HTML to a new file (optional)
with open("templates/output_AAPL.html", "w") as output_file:
  output_file.write(rendered_html)

print("Generated news webpage: output_AAPL.html")

with open("templates/about.html", "r") as template_file:
  template = Template(template_file.read())
  rendered_html = template.render(name = "ITC Limited",itc_news_html=itc_news_html, current_date=published_on)

# Write the rendered HTML to a new file (optional)
with open("templates/output_ITC.html", "w") as output_file:
  output_file.write(rendered_html)

print("Generated news webpage: output_ITC.html")

with open("templates/about.html", "r") as template_file:
  template = Template(template_file.read())
  rendered_html = template.render(name = "TATA Steel Limited",tata_news_html=tata_news_html, current_date=published_on)

# Write the rendered HTML to a new file (optional)
with open("templates/output_TATA.html", "w") as output_file:
  output_file.write(rendered_html)

print("Generated news webpage: output_TATA.html")
