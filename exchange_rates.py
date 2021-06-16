# exchange_rates.py

import requests

def get_exchange_rate(from_currency, to_currency):
    # Implement logic to fetch exchange rates from CurrencyLayer or Fixer.io
    # Use the API keys stored in api_key.txt
    # Example using CurrencyLayer API
    currency_layer_api_key = get_api_key("CURRENCYLAYER")
    currency_layer_url = f"https://api.currencylayer.com/live?access_key={currency_layer_api_key}"
    response = requests.get(currency_layer_url)
    data = response.json()

    if response.status_code == 200 and data["success"]:
        rates = data["quotes"]
        key = f"{from_currency}{to_currency}"
        if key in rates:
            return rates[key]
        else:
            return None
    else:
        # Handle API request error
        return None
def get_api_key(api_name):
    with open("api_key.txt", "r") as file:
        for line in file:
            if line.startswith(api_name):
