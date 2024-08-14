import pytest
from currency_converter import (output_all_currencies,
                                show_exchange_rate,
                                convert_value,
                                check_currency_codes)


lst_currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD']

api_data = {'data': {'AUD': 1.518340182,
                     'USD': 1,
                     'EUR': 0.9141001224,
                     'GBP': 0.7829601241,
                     'JPY': 146.9292393414,
                    }
            }


def test_output_all_currencies():
    output_str = 'AUD - Australian Dollar\nUSD - United States Dollar\nEUR - Euro\nGBP - British Pound Sterling\nJPY - Japanese Yen'
    assert output_all_currencies(api_data) == output_str


def test_show_exchange_rate():
    assert show_exchange_rate(api_data, "EUR") == 0.9141001224


def test_convert_value_valid():
    conversion_lst = ['100', 'USD', 'EUR']
    assert convert_value(api_data, conversion_lst, lst_currencies) == 91.41001224


@pytest.mark.parametrize('conv_lst, expected_error', [(['0', 'USD', 'EUR'], ValueError),
                                                      (['-10', 'USD', 'EUR'], ValueError),
                                                      (['-10', 'USD', 'USD'], ValueError),
                                                      (['-10', 'USD', 'KZT'], ValueError),
                                                      (['-10', 'RUB', 'KZT'], ValueError),
                                                      (['Hello', 'USD', 'AUD'], ValueError),

])
def test_convert_value_invalid(conv_lst, expected_error):
    with pytest.raises(expected_error):
        convert_value(api_data, conv_lst, lst_currencies)


def test_check_currency_codes_valid():
    conversion_lst = ['100', 'USD', 'EUR']
    assert check_currency_codes(conversion_lst, lst_currencies) == ('USD', 'EUR')


@pytest.mark.parametrize('conv_lst, expected_error', [(['100', 'USD', 'USD'], ValueError),
                                                      (['10', 'USD', 'KZT'], ValueError),
                                                      (['5', 'RUB', 'KZT'], ValueError),

])
def test_check_currency_codes_invalid(conv_lst, expected_error):
    with pytest.raises(expected_error):
        convert_value(api_data, conv_lst, lst_currencies)

