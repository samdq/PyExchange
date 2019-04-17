# pyexchange.py

import requests
from exchange_rates import get_exchange_rate

def convert_currency(amount, from_currency, to_currency):
    