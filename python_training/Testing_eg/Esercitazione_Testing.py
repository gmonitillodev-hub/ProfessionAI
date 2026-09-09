import requests
import unittest
from unittest.mock import patch, MagicMock


def factorial(n):
    if n < 0:
        raise ValueError("Il numero deve essere positivo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_factorial(self):
        self.assertRaises(ValueError, factorial, -12)


class CurrencyConverter:

    def __init__(self, api_url):
        self.api_url = api_url

    def get_exchange_rate(self, from_currency, to_currency):
        response = requests.get({f"{self.api_url}?from={from_currency}&to={to_currency}"})
        if response.status_code != 200:
            raise Exception(f"Errore nella chiamata API")
        data = response.json()
        return data["rates"][to_currency]


def exchange_side_effect(from_currency, to_currency):
    if from_currency == 'euro' and to_currency == 'usd':
        return 1
    elif from_currency == 'euro' and to_currency == 'pln':
        return 0.5
    else:
        raise Exception(f"Currency {from_currency} is not supported")


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self) -> None:
        self.api_url = "http://127.0.0.1:8000"
        print("Setting up -> " + self.api_url)
        self.converter = CurrencyConverter(self.api_url)

    @patch.object(CurrencyConverter, "get_exchange_rate",
                  side_effect=lambda from_cur, to_cur: exchange_side_effect(from_cur, to_cur))
    def test_exchange_rate(self, mock_exchange_rate: MagicMock):
      response =  self.converter.get_exchange_rate( "euro", "pln")
      print(response)

      self.assertTrue(mock_exchange_rate.called)
      self.assertRaises(Exception, self.converter.get_exchange_rate, "euro", "pln")