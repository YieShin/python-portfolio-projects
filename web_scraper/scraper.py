import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website (practice site for scraping)
URL = "http://quotes.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Collect data
quotes = []
authors = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.get_text())

for author in soup.find_all("small", class_="author"):
    authors.append(author.get_text())

# Save into DataFrame
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

# Save to CSV
df.to_csv("quotes.csv", index=False)

print("✅ Scraping complete! Quotes saved to quotes.csv")