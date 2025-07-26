# Insider Trades Fetcher – Yahoo Finance (via RapidAPI)

## Description

This script fetches **insider trading data** for a list of popular stock symbols using the **Yahoo Finance API** through **RapidAPI**. It loops through multiple tickers, retrieves insider trade records, and saves the results in a CSV file.

Ideal for financial analysts, data scientists, or investors looking to monitor insider trading behavior.

## Features

- Fetches insider trades for multiple stocks (e.g., AAPL, MSFT, AMZN)
- Handles API errors and network failures
- Uses `time.sleep()` to respect API rate limits
- Saves the results in CSV file

## Technologies Used

- Python
- `requests` (HTTP requests)
- `csv` (CSV file generation)
- `time` (rate limit handling)
- [RapidAPI](https://rapidapi.com/) to access the Yahoo Finance API

## Usage Guide

Run the script using Python:

```bash
python insider_trades_fetcher.py
```

It will:
- Loop through a list of stock symbols
- Send an API request for each symbol
- Save all the insider trade records into a file named `insider_trades_all.csv`

## Project Structure

```
insider-trades-fetcher/
├── insider_trades_fetcher.py    # Main Python script
├── insider_trades_all.csv       # Output file (auto-generated)
├── README.md                    # Project documentation
```

## RapidAPI Notes

- Sign up at [RapidAPI](https://rapidapi.com/)
- Subscribe to the **Yahoo Finance API** plan
- Get your **API key** and update it in the script

## Legal Disclaimer

The data provided is for **educational and research purposes only**. Please review the API provider’s **terms of use** and ensure you’re compliant with their policies before using the data commercially or in production.

## 📬 Contact Information

**Developer:** Cyrus Wambugu  
**LinkedIn:** [linkedin.com/in/cyrus-wambugu-b9476195](https://www.linkedin.com/in/cyrus-wambugu-b9476195)  
**Email:** cyruswambugu91@gmail.com
