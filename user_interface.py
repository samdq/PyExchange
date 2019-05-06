# user_interface.py

from pyexchange import convert_currency
if __name__ == "__main__":
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ")
    to_currency = input("Enter the target currency code: ")

    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

