from currency_converter import output_all_currencies



api_data = {'data': {'AUD': 1.518340182,
                     'BGN': 1.787220253,
                     'BRL': 5.4922310083
                    }
            }


def test_output_all_currencies():
    output_str = 'AUD - Australian Dollar\nBGN - Bulgarian Lev\nBRL - Brazilian Real'
    assert output_all_currencies(api_data) == output_str
