# CURRENCY CONVERSION TOOL
#### Description:

This is a command-line tool that allows you to retrieve and convert currency exchange rates using the FreeCurrencyAPI.
The tool supports various operations, such as displaying all available currencies, showing the exchange rate of a specific currency against USD,
and converting amounts from one currency to another.

Features:
Show All Currencies: Display a list of all available currencies with their respective currency codes.
Exchange Rate: Retrieve and display the exchange rate of a specified currency against USD.
Currency Conversion: Convert a specified amount from one currency to another.

Requirements:
Python 3.7 or higher
Install dependecies (pip install -r requirements.txt)

Usage:

1. Show All Available Currencies
To display a list of all available currencies run the following command:

$ python project.py --all / -a

This will print out all currency codes along with their names.

2. Get Exchange Rate of a Currency
To retrieve the exchange rate of a specific currency against the USD run the following command:

$ python project.py --rate CURRENCY_CODE / -r CURRENCY_CODE

For example, to get the exchange rate of EUR:

$ python project.py --rate EUR

3. Convert Currency
To convert an amount from one currency to another run the following command:

$ python project.py --convert AMOUNT FROM_CURRENCY TO_CURRENCY or -c AMOUNT FROM_CURRENCY TO_CURRENCY

For example, to convert 100 USD to EUR:

$ python project.py --convert 100 USD EUR


Help
To display the help message and view all available options run the following command:

$ python project.py --help or -h

The help message will also be displayed if you don't provide any arguments.

Error Handling:
The tool will raise an error if you try to convert currencies that are not available or enter an invalid currency code.
If you input an invalid amount (e.g., a negative number), the tool will prompt you to enter a positive amount.

Testing
This application was tested with pytest.
Unit tests were created for the key functions, including argument parsing, currency conversion, and error handling.
