# CryptoAPI

---

## Setup

### 3rd party api hookup
The API hits the coinmarketcap api. In order to do that you need an API Key. 

The API Key isn't stored here, you'll have to get your own.
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

---

### Initial Local Setup
This project uses the virtual environment model for python execution. 

1. Create a virtual environment (with the name "env")
> python3 -m venv env

2. Activate that environment 

##### If you're on a Mac (and maybe linux (untested)) run this in your terminal
> source env/bin/activate

##### ...And if you're on Windows (using Powershell)
> .\env\Scripts\Activate.ps1

If you run into any trouble executing the above command, run the following command in your powershell, then retry the above command
> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

3. Install necessary external library dependencies by running the following command inside the virtual environment
> pip install -r Dependencies.txt 

()()()
#### run the command inside of the environment "deactivate" and you'll be exited gracefully

---

## Testing
From the root of the project run

### On mac
> python3 -m unittest discover . "*_test.py"

### On Windows
> python -m unittest discover . "*_test.py"


> python -m unittest discover ./HowItDoesIt/Databridge "Databridge_test.py"

