import json

def getApiKeySecrets():
    file = open("CoinMarketCapApi/secrets.json", "r")
    secrets = json.load(file)
    file.close()
    return secrets["api-key"]

def getCryptosOfInterest():
    file = open("Database/CryptosOfInterest.txt", "r")
    cryptos = file.read()
    file.close()
    return cryptos