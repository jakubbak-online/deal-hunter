
# deal-hunter - OLX.pl sniping tool

## What is deal-hunter?

deal-hunter is a sniping tool for OLX.pl (polish craigslist-like site). \
It takes .csv file as an input with search information, and telegram bot API to send notifications.

#### Requirements

- Python 3.11
- Telegram (user account, and Bot API key)

#### Optional requirements
- Git (for installation purposes)

## Installation and use

To install deal-hunter you can use following commands in cmd, in preferred directory: 

```commandline
git clone https://github.com/jakubbak-online/deal-hunter.git
cd deal-hunter
pip install -r requirements.txt
```

Now, update ```./src/config.py``` with your Telegram Bot API key, and Telegram user id. \
You can use this guide to go through generating Bot API key: [**Link**](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

Then, modify search data in ```./src/data/data_long.csv```, or specify other location of csv file with info about searches.

You can now use following commands, and it continuously will go through list of your offers, sending message to user specified in config with every new offer seen: 
 
```commandline
 cd ./src/
 py main.py
```

*NOTE: on the first run through new search it will notify you of **all** offers in that search - it has no previous data about searches done to compare to!*

\
It's still an early version, so **I'd much appreciate if you'd report all bugs you encounter!**
Suggestion are also welcome!

