import requests
import json
from bs4 import BeautifulSoup

url = 'https://bank.gov.ua/markets/exchangerates'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', id='exchangeRates')

if table:
    exchange_rates = {}

    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        currency_symbol = cells[1].text.strip()
        currency_name = cells[3].text.strip()
        exchange_rate = float(cells[4].text.strip().replace(',', '.'))
        exchange_rates[currency_symbol] = {
            'name': currency_name,
            'rate': exchange_rate
        }

    to_currency_symbol = input("Enter the currency symbol to convert to: ").upper()
    amount = float(input("Enter the amount in UAH: "))

    if to_currency_symbol in exchange_rates:
        to_rate = exchange_rates[to_currency_symbol]['rate']
        converted_amount = amount / to_rate
        print(f"{amount} UAH = {round(converted_amount, 2)} {exchange_rates[to_currency_symbol]['name']} ({to_currency_symbol})")
    else:
        print("Incorrect currency symbol entered.")
else:
    print("Unable to find the currency exchange rates table.")







top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
top_stories_response = requests.get(top_stories_url)
top_stories_ids = top_stories_response.json() if top_stories_response.status_code == 200 else None

if top_stories_ids:
    print("List of Article IDs:")

    for article_id in top_stories_ids[:20]:
        article_url = f"https://hacker-news.firebaseio.com/v0/item/{article_id}.json"
        article_response = requests.get(article_url)
        article_data = article_response.json() if article_response.status_code == 200 else None

        if article_data:
            print("Article ID:", article_id)
            print("Title:", article_data.get("title"))
            print("Author:", article_data.get("by"))
            print("Score:", article_data.get("score"))
            print("URL:", article_data.get("url"))
            print("-" * 30)
        else:
            print(f"No data found for article with ID {article_id}")
else:
    print("Failed to fetch the list of article IDs.")
