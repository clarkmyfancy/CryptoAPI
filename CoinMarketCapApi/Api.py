from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from DataBridge.DataBridge import getApiKeySecrets, getCryptosOfInterest


class Api:

    def __init__(self):

        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': getApiKeySecrets(),
        }
        self.session = Session()
        self.session.headers.update(self.headers)

        self.cryptos_of_interest = getCryptosOfInterest()


    def getQuotes(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  
        
        parameters = {
            'symbol': self.cryptos_of_interest
        }
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            self.parse_out_tickers_and_prices(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        
    
    def parse_out_tickers_and_prices(self, data):
        tickers = self.cryptos_of_interest.split(",")

        for ticker in tickers:
            self.print_ticker_and_price(data, ticker)
    
    def print_ticker_and_price(self, data, ticker):
        price = data['data'][ticker]['quote']['USD']['price']
        print(ticker + ": " + str(round(price, 2)))