import argparse
import requests
import json
from currencies import currency_dict
import sys
from config import API_KEY


def api_parse(api_url, API_KEY):
    url = api_url
    params = {"apikey": API_KEY}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        raise ValueError("Information not found")


def create_parser(lst_currencies):
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

    return parser


def make_lst_currencies(data):
    lst_currencies = list(data['data'].keys())
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
            if cur_code not in lst_currencies:
                raise ValueError
    except ValueError:
        sys.exit(f"Currency {cur_code} cannot be converted. Choose from the available currencies.")
    else:
        if currency_in != currency_out:
            return (currency_in, currency_out)
        else:
            sys.exit(f"You must enter two different currency codes. Example: USD AUD")


def main(url, API_KEY):
    data = api_parse(url, API_KEY)
    lst_currencies = make_lst_currencies(data)
    parser = create_parser(lst_currencies)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

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
    api_url = "https://api.freecurrencyapi.com/v1/latest"
    API_KEY = API_KEY
    main(api_url, API_KEY)
