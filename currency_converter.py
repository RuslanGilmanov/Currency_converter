import argparse
import requests
import json
from currencies import currency_dict
import sys


lst_currencies = []


def api_parse():
    url = "https://api.freecurrencyapi.com/v1/latest"
    params = {"apikey": "fca_live_H1uIqNDvfJMVIlGuaZnEcZXlJU1iKFWLtoFJGxoC"}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print(f"Information not found")


def create_parser():
    parser = argparse.ArgumentParser(description="Currency Conversion Tool")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Show all available currencies")
    parser.add_argument("-r","--rate",metavar="CURRENCY_CODE",dest="currency_code",
        choices=lst_currencies,
        help="Enter a currency code to see its current exchange rate against the USD. "
             f"Valid choices are: {lst_currencies}")
    parser.add_argument("-c","--convert", nargs=3, dest="conversion_lst",
                        metavar=("Amount","Currency_1","Currency_2"),
                        help="Convert the amount from Curency_1 to Currency_2")
    args = parser.parse_args()
    return args


def make_lst_currencies(data): 
    for item in data['data']:
        lst_currencies.append(item)
    return lst_currencies


def output_all_currencies(data):
    for item in data['data']:
        if item in currency_dict.keys():
            print(f"{item} - {currency_dict[item]}")


def show_exchange_rate(data, currency_code):
    exchange_rate = data['data'][currency_code]
    return exchange_rate


def convert_value(data, conversion_lst):
    try:
        initial_amount = float(conversion_lst[0])
        if initial_amount < 0:
            sys.exit("The amount is negative. Enter positive amount")
        from_currency, to_currency = check_currency_codes(conversion_lst)
    except ValueError:
        sys.exit("Entered amount is not a number. Examples: 100, 34.50")
    else:
        converted_amount = (initial_amount / data['data'][from_currency]) * \
                           data['data'][to_currency]
    return converted_amount


def check_currency_codes(conversion_lst):
    currency_in = conversion_lst[1]
    currency_out = conversion_lst[2]
    try:
        for cur_code in conversion_lst[1:]:
            cur_code in lst_currencies
    except ValueError:
        sys.exit(f"The currency code {cur_code} is not on the list")
    else:
        if currency_in != currency_out:
            return (currency_in, currency_out)
        else:
            sys.exit(f"You must enter different currency codes. Example: USD AUD")


def main():
    data = api_parse()
    lst_currencies = make_lst_currencies(data)
    args = create_parser()
    if args.all:
        output_all_currencies(data)
    if args.currency_code:
        currency_code = args.currency_code
        exchange_rate = show_exchange_rate(data, currency_code)
        print(f"Exchange rate of the {args.currency_code} is {exchange_rate:.3f} against the USD")
    if args.conversion_lst:
        conversion_lst = args.conversion_lst
        value = convert_value(data, conversion_lst)
        print(f"{conversion_lst[0]} {conversion_lst[1]} is {value:.2f} {conversion_lst[2]}")


if __name__ == "__main__":
    main()
