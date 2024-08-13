import pytest
import argparse
from currency_converter import create_parser, main
from config import API_KEY

lst_currencies = ['USD', 'EUR', 'JPY', 'GBP']

def test_parser_all():
    parser = create_parser(lst_currencies)
    args = parser.parse_args(['--all'])
    assert args.all == True
    assert args.currency_code == None
    assert args.conversion_lst == None


def test_parser_rate_valid():
    parser = create_parser(lst_currencies)
    args = parser.parse_args(['--rate', 'USD'])
    assert args.all == False
    assert args.currency_code == 'USD'
    assert args.conversion_lst == None


def test_parser_rate_invalid():
    parser = create_parser(lst_currencies)
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--r', 'KZT'])


def test_parser_convert():
    parser = create_parser(lst_currencies)
    args = parser.parse_args(['--convert', '100', 'USD', 'AUD'])
    assert args.all == False
    assert args.currency_code == None
    assert args.conversion_lst == ['100', 'USD', 'AUD']


def test_parser_no_arguments():
    api_url = "https://api.freecurrencyapi.com/v1/latest"
    parser = create_parser(lst_currencies)
    args = parser.parse_args([])
    with pytest.raises(SystemExit):
        main(api_url, API_KEY)
