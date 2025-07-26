
"""
Script Name: insider_trades_fetcher.py

Description:
This script retrieves insider trading data from the Yahoo Finance API (via RapidAPI).
It loops through a list of stock symbols, makes API requests for each one,
handles errors, and prints or stores the results.

Features:
- Uses `requests` to query the API.
- Handles exceptions like network errors or bad JSON responses.
- Respects API rate limits using `time.sleep()`.
"""

import requests
import csv
import time

# API details
url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/insider-trades"
headers = {
    "x-rapidapi-key": "80910b1661mshb52d67e398c9061p16b43cjsn7bdbeaf15d31",
    "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
}

# Symbols to query
symbols = ["AAPL", "NVDA", "MSFT", "AMZN", "META", "2222", "AVGO", "TSM", "BRK.A", "GOOGL"]

# Collect all trades
all_trades = []

for symbol in symbols:
    querystring = {"symbol": symbol}
    print(f"Fetching data for {symbol}...")

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if data['meta']['status'] == 200:
            trades = data['body']
            all_trades.extend(trades)
        else:
            print(f"Error for {symbol}: {data.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"Request failed for {symbol}: {e}")# Catches any kind of error to ensure sript doesnt crash

    time.sleep(1)  # to avoid API rate limit

# Save all trades to CSV
if all_trades:
    csv_filename = "insider_trades_all.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=all_trades[0].keys())
        writer.writeheader()
        writer.writerows(all_trades)

    print(f"\nSaved {len(all_trades)} trades to '{csv_filename}'")
else:
    print("No trades found.")
