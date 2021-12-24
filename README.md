# CryptoAPI


### Setup
The API hits the coinmarketcap api. In order to do that you need an API Key. 

For security reasons, an API key should not be stored in the code repo, so you have to get your own.
1. Go to [the CoinMarketCap API website](https://coinmarketcap.com/api/) and login to your Developers account. If you don't have one then create an account. 
2. When you get logged in, go to the Overview Panel and find the API Key. The api won't work without it.  Copy The API key 
3. Take that key and now in the project directory, navigate to CryptoAPI/CoinMarketCapApi and create a file called "secrets.json"
4. Add the following code to that file.

```
{
  "api-key": ""
}

```
5. Copy the API Key you got from the CoinMarketCap site and paste it between the quotes. 
6. Save that and now the api will work
