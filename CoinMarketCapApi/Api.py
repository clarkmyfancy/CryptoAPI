from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from CoinMarketCapApi.Helpers import create_comma_seperated_string_from_list_of_strings
import secrets

class Api:

    def __init__(self):
        secrets = self.loadApiSecrets()
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': secrets["api-key"],
        }
        self.session = Session()
        self.session.headers.update(self.headers)

        self.cryptos_of_interest = [
            "BTC",
            "ETH",
            "ADA",
            "LTC",
            "SOL",
            "HBAR",
            "DOT",
            "CHZ",
            "AVAX",
            "DOGE",
            "MATIC"
        ]

    def loadApiSecrets(self):
        file = open("CoinMarketCapApi/secrets.json")
        secrets = json.load(file)
        file.close()
        return secrets


    def getQuotes(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  

        cryptos = create_comma_seperated_string_from_list_of_strings(self.cryptos_of_interest)
        parameters = {
            'symbol': cryptos
        }
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            self.parse_out_tickers_and_prices(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        
    
    def parse_out_tickers_and_prices(self, data):
        print()
        for ticker in self.cryptos_of_interest:
            self.print_ticker_and_price(data, ticker)
    
    def print_ticker_and_price(self, data, ticker):
        price = data["data"][ticker]['quote']['USD']['price']
        print(ticker + ": " + str(round(price, 2)))




    

