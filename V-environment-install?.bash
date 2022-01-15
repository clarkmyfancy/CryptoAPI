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
