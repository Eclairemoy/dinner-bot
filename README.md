# dinner-bot

- make sure you nave ngrok installed
- create a new virtual env by running `python3 -m venv venv`
- install the requirements by running `pip3 install -r requirements.txt`
- create `.flaskenv` and put in the following 
```
FLASK_APP=app/main.py
FLASK_ENV=development
FLASK_SECRET_KEY=1234
FLASK_RUN_PORT=8000
```   
- Buy a twilio number
- Set up a twilio messaging service
- add environment variables for `ACCOUNT_SID`, `AUTH_TOKEN`, and `MESSAGING_SERVICE_SID`
- set `organizers_phone_num` to be your personal number/the number you will use for testing
- set `family_nums` to be the list of family members' numbers you want to use
- fill in the stubbed out functions/update the scheduled time
- go to where your ngrok is installed and run `./ngrok http 8000`
- copy the url and paste it along with the endpoint into you twilio number console ie `https://x0x0x0x0.ngrok.io/send-rec`
