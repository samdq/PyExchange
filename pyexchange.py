# pyexchange.py

import requests
from exchange_rates import get_exchange_rate

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

if __name__ == "__main__":
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ")
    to_currency = input("Enter the target currency code: ")

    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")