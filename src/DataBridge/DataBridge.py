import json

def getApiKeySecrets():
    file = open("src/CoinMarketCapApi/secrets.json", "r")
    secrets = json.load(file)
    file.close()
    return secrets["api-key"]

def getCryptosOfInterest():
    file = open("src/Database/CryptosOfInterest.txt", "r")
    cryptos = file.read()
    file.close()
    return cryptos

def addToCryptosOfInterest(ticker):
    file = open("src/Database/CryptosOfInterest.txt", "a")
    thing = str(',' + ticker)
    file.write(thing)
    file.close()