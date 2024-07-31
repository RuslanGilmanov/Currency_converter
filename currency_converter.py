import argparse
import requests
import json
from currencies import currency_lst


def create_parser():
    parser = argparse.ArgumentParser(description="USD converter")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Prints out all available currencies")
    parser.add_argument("-c", "--currency", help="")
    args = parser.parse_args()
    return args


def api_parse():
    url = "https://api.freecurrencyapi.com/v1/latest"
    params = {"apikey": "fca_live_H1uIqNDvfJMVIlGuaZnEcZXlJU1iKFWLtoFJGxoC"}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print(f"Information not found")


def output_all_currencies(data):
    for item in data['data']:
        if item in currency_lst.keys():
            print(f"{item} - {currency_lst[item]}")


def main():
    args = create_parser()
    data = api_parse()
    if args.all:
        output_all_currencies(data)


if __name__ == "__main__":
    main()

