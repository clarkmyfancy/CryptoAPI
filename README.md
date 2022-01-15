# CryptoAPI


### Setup

### 3rd party api hookup
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

### project setup


# this will get everything setup for you to use this program on any computer

# create a virtual environment
python3 -m venv env

# activate that environment 
## on a mac (and maybe linux (untested))
source env/bin/activate

## on windows

// you might have to run this command to modify your script execution policy
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
``` 
then run -> `.\env\Scripts\Activate.ps1` and you should be in the necessary virtual environment

# install necessary packages
// inside the new environment you just setup run the command -> pip install -r Dependencies.txt 

# when you're all done
# run the command inside of the environment "deactivate" and you'll be good to go

## Testing
in the root directory -> 
python3 -m unittest discover . "*_test.py"

